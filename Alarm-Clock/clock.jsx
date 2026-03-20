import { useState, useEffect, useRef, useCallback } from "react";

const DAYS = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
const SNOOZE_MINUTES = 5;

function generateId() {
  return Math.random().toString(36).slice(2, 9);
}

function pad(n) {
  return String(n).padStart(2, "0");
}

function formatTime12(h, m) {
  const ampm = h >= 12 ? "PM" : "AM";
  const h12 = h % 12 === 0 ? 12 : h % 12;
  return `${h12}:${pad(m)} ${ampm}`;
}

function parseTime(str) {
  const [h, m] = str.split(":").map(Number);
  return { h, m };
}

function addMinutes(h, m, mins) {
  const total = h * 60 + m + mins;
  return { h: Math.floor(total / 60) % 24, m: total % 60 };
}

const SOUNDS = [
  { id: "beep", label: "Classic Beep" },
  { id: "chime", label: "Soft Chime" },
  { id: "pulse", label: "Pulse" },
];

function useAudioEngine() {
  const ctxRef = useRef(null);

  function getCtx() {
    if (!ctxRef.current) ctxRef.current = new (window.AudioContext || window.webkitAudioContext)();
    return ctxRef.current;
  }

  function playBeep(ctx, t) {
    const osc = ctx.createOscillator();
    const gain = ctx.createGain();
    osc.connect(gain); gain.connect(ctx.destination);
    osc.type = "square";
    osc.frequency.setValueAtTime(880, t);
    gain.gain.setValueAtTime(0.3, t);
    gain.gain.exponentialRampToValueAtTime(0.001, t + 0.18);
    osc.start(t); osc.stop(t + 0.18);
  }

  function playChime(ctx, t) {
    [523, 659, 784, 1047].forEach((freq, i) => {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.connect(gain); gain.connect(ctx.destination);
      osc.type = "sine";
      osc.frequency.value = freq;
      const st = t + i * 0.15;
      gain.gain.setValueAtTime(0, st);
      gain.gain.linearRampToValueAtTime(0.25, st + 0.05);
      gain.gain.exponentialRampToValueAtTime(0.001, st + 0.6);
      osc.start(st); osc.stop(st + 0.6);
    });
  }

  function playPulse(ctx, t) {
    for (let i = 0; i < 3; i++) {
      const osc = ctx.createOscillator();
      const gain = ctx.createGain();
      osc.connect(gain); gain.connect(ctx.destination);
      osc.type = "sawtooth";
      osc.frequency.value = 440;
      const st = t + i * 0.22;
      gain.gain.setValueAtTime(0.2, st);
      gain.gain.exponentialRampToValueAtTime(0.001, st + 0.18);
      osc.start(st); osc.stop(st + 0.2);
    }
  }

  function playSound(soundId) {
    const ctx = getCtx();
    if (ctx.state === "suspended") ctx.resume();
    const t = ctx.currentTime;
    if (soundId === "beep") { for (let i = 0; i < 4; i++) playBeep(ctx, t + i * 0.25); }
    else if (soundId === "chime") playChime(ctx, t);
    else if (soundId === "pulse") playPulse(ctx, t);
  }

  return { playSound };
}

const INITIAL_ALARMS = [
  { id: generateId(), hour: 7, minute: 0, label: "Wake Up", enabled: true, days: [1,2,3,4,5], sound: "chime", snoozeCount: 0 },
  { id: generateId(), hour: 9, minute: 30, label: "Weekend Brunch", enabled: false, days: [0,6], sound: "beep", snoozeCount: 0 },
];

export default function AlarmClock() {
  const [now, setNow] = useState(new Date());
  const [alarms, setAlarms] = useState(INITIAL_ALARMS);
  const [firing, setFiring] = useState(null); // { alarm, snoozedUntil? }
  const [editingId, setEditingId] = useState(null);
  const [showAdd, setShowAdd] = useState(false);
  const [newAlarm, setNewAlarm] = useState({ hour: 8, minute: 0, label: "", days: [1,2,3,4,5], sound: "beep" });
  const [flash, setFlash] = useState(false);
  const { playSound } = useAudioEngine();
  const ringIntervalRef = useRef(null);
  const lastFiredRef = useRef({});

  useEffect(() => {
    const t = setInterval(() => setNow(new Date()), 1000);
    return () => clearInterval(t);
  }, []);

  useEffect(() => {
    if (flash) { const t = setTimeout(() => setFlash(false), 600); return () => clearTimeout(t); }
  }, [flash]);

  // Alarm check
  useEffect(() => {
    if (firing) return;
    const h = now.getHours(), m = now.getMinutes(), s = now.getSeconds(), d = now.getDay();
    if (s !== 0) return;
    for (const alarm of alarms) {
      if (!alarm.enabled) continue;
      if (!alarm.days.includes(d)) continue;
      if (alarm.hour !== h || alarm.minute !== m) continue;
      const key = `${alarm.id}-${now.toDateString()}-${h}:${m}`;
      if (lastFiredRef.current[key]) continue;
      lastFiredRef.current[key] = true;
      setFiring({ alarm });
      return;
    }
  }, [now, alarms, firing]);

  // Ring sound loop
  useEffect(() => {
    if (!firing) { clearInterval(ringIntervalRef.current); return; }
    setFlash(true);
    playSound(firing.alarm.sound);
    ringIntervalRef.current = setInterval(() => {
      playSound(firing.alarm.sound);
      setFlash(f => !f);
    }, 1500);
    return () => clearInterval(ringIntervalRef.current);
  }, [firing]);

  const dismissAlarm = useCallback(() => {
    setFiring(null);
    setFlash(false);
  }, []);

  const snoozeAlarm = useCallback(() => {
    if (!firing) return;
    const { h, m } = addMinutes(now.getHours(), now.getMinutes(), SNOOZE_MINUTES);
    setAlarms(prev => prev.map(a => a.id === firing.alarm.id
      ? { ...a, snoozeCount: (a.snoozeCount || 0) + 1 }
      : a));
    setFiring(null);
    setFlash(false);
    // Create a temporary one-shot snooze alarm
    const snoozeId = `snooze-${firing.alarm.id}`;
    const base = firing.alarm;
    const snoozed = { ...base, id: snoozeId, hour: h, minute: m, days: [now.getDay()], label: `${base.label} (snoozed)`, _oneShot: true, snoozeCount: 0 };
    setAlarms(prev => [...prev.filter(a => a.id !== snoozeId), snoozed]);
  }, [firing, now]);

  function toggleAlarm(id) {
    setAlarms(prev => prev.map(a => a.id === id ? { ...a, enabled: !a.enabled } : a));
  }

  function deleteAlarm(id) {
    setAlarms(prev => prev.filter(a => a.id !== id));
    if (firing?.alarm.id === id) setFiring(null);
  }

  function addAlarm() {
    if (!newAlarm.days.length) return;
    setAlarms(prev => [...prev, { ...newAlarm, id: generateId(), enabled: true, snoozeCount: 0 }]);
    setShowAdd(false);
    setNewAlarm({ hour: 8, minute: 0, label: "", days: [1,2,3,4,5], sound: "beep" });
  }

  function saveEdit(id) {
    setAlarms(prev => prev.map(a => a.id === id ? { ...a, ...editForm } : a));
    setEditingId(null);
  }

  const [editForm, setEditForm] = useState({});
  function startEdit(alarm) {
    setEditForm({ hour: alarm.hour, minute: alarm.minute, label: alarm.label, days: [...alarm.days], sound: alarm.sound });
    setEditingId(alarm.id);
  }

  const hours = now.getHours(), mins = now.getMinutes(), secs = now.getSeconds();
  const secDeg = secs * 6;
  const minDeg = mins * 6 + secs * 0.1;
  const hrDeg = (hours % 12) * 30 + mins * 0.5;

  const sortedAlarms = [...alarms].sort((a, b) => a.hour * 60 + a.minute - (b.hour * 60 + b.minute));

  return (
    <div style={{ minHeight: "100vh", background: "#0a0a0f", color: "#e8e8f0", fontFamily: "'Courier New', monospace", padding: "2rem 1rem" }}>
      {/* Firing overlay */}
      {firing && (
        <div style={{
          position: "fixed", inset: 0, zIndex: 1000,
          background: flash ? "rgba(255,60,60,0.18)" : "rgba(0,0,0,0.85)",
          display: "flex", alignItems: "center", justifyContent: "center",
          transition: "background 0.3s"
        }}>
          <div style={{
            background: "#13131f", border: `2px solid ${flash ? "#ff4444" : "#444"}`,
            borderRadius: 20, padding: "2.5rem 3rem", textAlign: "center", maxWidth: 360,
            boxShadow: flash ? "0 0 60px rgba(255,60,60,0.4)" : "none",
            transition: "border-color 0.3s, box-shadow 0.3s"
          }}>
            <div style={{ fontSize: 48, marginBottom: 8 }}>⏰</div>
            <div style={{ fontSize: 28, fontWeight: "bold", letterSpacing: 2, color: "#ff6666", marginBottom: 4 }}>
              {formatTime12(firing.alarm.hour, firing.alarm.minute)}
            </div>
            <div style={{ fontSize: 16, color: "#aaa", marginBottom: 28, minHeight: 22 }}>
              {firing.alarm.label || "Alarm"}
            </div>
            <div style={{ display: "flex", gap: 16, justifyContent: "center" }}>
              <button onClick={snoozeAlarm} style={{
                padding: "10px 24px", borderRadius: 10, border: "1px solid #555",
                background: "#1e1e2e", color: "#ccc", cursor: "pointer", fontSize: 14, letterSpacing: 1
              }}>
                ZZZ {SNOOZE_MINUTES}min
              </button>
              <button onClick={dismissAlarm} style={{
                padding: "10px 24px", borderRadius: 10, border: "none",
                background: "#ff4444", color: "#fff", cursor: "pointer", fontSize: 14, letterSpacing: 1, fontWeight: "bold"
              }}>
                DISMISS
              </button>
            </div>
          </div>
        </div>
      )}

      <div style={{ maxWidth: 520, margin: "0 auto" }}>
        {/* Header clock */}
        <div style={{ textAlign: "center", marginBottom: "2.5rem" }}>
          <div style={{ display: "flex", alignItems: "center", justifyContent: "center", gap: 32, marginBottom: 12 }}>
            {/* Analog clock */}
            <svg width="110" height="110" viewBox="0 0 110 110">
              <circle cx="55" cy="55" r="52" fill="#13131f" stroke="#2a2a3e" strokeWidth="2" />
              {[...Array(12)].map((_, i) => {
                const a = (i * 30 - 90) * Math.PI / 180;
                const r1 = i % 3 === 0 ? 42 : 44;
                return <line key={i}
                  x1={55 + r1 * Math.cos(a)} y1={55 + r1 * Math.sin(a)}
                  x2={55 + 48 * Math.cos(a)} y2={55 + 48 * Math.sin(a)}
                  stroke={i % 3 === 0 ? "#6060aa" : "#333"} strokeWidth={i % 3 === 0 ? 2 : 1} />;
              })}
              {/* hour */}
              <line x1="55" y1="55"
                x2={55 + 28 * Math.cos((hrDeg - 90) * Math.PI / 180)}
                y2={55 + 28 * Math.sin((hrDeg - 90) * Math.PI / 180)}
                stroke="#c8c8e8" strokeWidth="3" strokeLinecap="round" />
              {/* minute */}
              <line x1="55" y1="55"
                x2={55 + 38 * Math.cos((minDeg - 90) * Math.PI / 180)}
                y2={55 + 38 * Math.sin((minDeg - 90) * Math.PI / 180)}
                stroke="#a0a0d0" strokeWidth="2" strokeLinecap="round" />
              {/* second */}
              <line x1="55" y1="55"
                x2={55 + 40 * Math.cos((secDeg - 90) * Math.PI / 180)}
                y2={55 + 40 * Math.sin((secDeg - 90) * Math.PI / 180)}
                stroke="#ff4466" strokeWidth="1" strokeLinecap="round" />
              <circle cx="55" cy="55" r="3" fill="#ff4466" />
            </svg>
            {/* Digital */}
            <div>
              <div style={{ fontSize: 44, fontWeight: "bold", letterSpacing: 3, color: "#e0e0ff", lineHeight: 1 }}>
                {pad(hours)}:{pad(mins)}
                <span style={{ fontSize: 22, color: "#7070aa", marginLeft: 4 }}>:{pad(secs)}</span>
              </div>
              <div style={{ fontSize: 13, color: "#6060aa", marginTop: 4, letterSpacing: 2 }}>
                {now.toLocaleDateString("en-US", { weekday: "long", month: "short", day: "numeric" }).toUpperCase()}
              </div>
            </div>
          </div>
        </div>

        {/* Alarms list */}
        <div style={{ marginBottom: "1.5rem" }}>
          <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 12 }}>
            <span style={{ fontSize: 11, letterSpacing: 3, color: "#6060aa" }}>ALARMS ({alarms.filter(a => !a._oneShot).length})</span>
            <button onClick={() => setShowAdd(s => !s)} style={{
              background: showAdd ? "#2a2a3e" : "#1a1a2e", border: "1px solid #3a3a5e",
              color: "#a0a0d8", borderRadius: 8, padding: "6px 16px", cursor: "pointer", fontSize: 12, letterSpacing: 1
            }}>
              {showAdd ? "CANCEL" : "+ NEW ALARM"}
            </button>
          </div>

          {/* Add alarm form */}
          {showAdd && (
            <div style={{ background: "#12121e", border: "1px solid #2a2a4e", borderRadius: 14, padding: "1.2rem", marginBottom: 12 }}>
              <AlarmForm
                form={newAlarm}
                onChange={setNewAlarm}
                onSave={addAlarm}
                onCancel={() => setShowAdd(false)}
                saveLabel="ADD ALARM"
              />
            </div>
          )}

          {sortedAlarms.filter(a => !a._oneShot).map(alarm => (
            <div key={alarm.id} style={{
              background: alarm.enabled ? "#12121e" : "#0d0d16",
              border: `1px solid ${alarm.enabled ? "#2a2a4e" : "#1a1a2a"}`,
              borderRadius: 14, padding: "1rem 1.2rem", marginBottom: 10,
              opacity: alarm.enabled ? 1 : 0.55, transition: "all 0.2s"
            }}>
              {editingId === alarm.id ? (
                <AlarmForm
                  form={editForm}
                  onChange={setEditForm}
                  onSave={() => saveEdit(alarm.id)}
                  onCancel={() => setEditingId(null)}
                  saveLabel="SAVE"
                />
              ) : (
                <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                  <div style={{ flex: 1 }}>
                    <div style={{ fontSize: 26, fontWeight: "bold", letterSpacing: 2, color: alarm.enabled ? "#d0d0f8" : "#666" }}>
                      {formatTime12(alarm.hour, alarm.minute)}
                    </div>
                    <div style={{ display: "flex", gap: 6, alignItems: "center", marginTop: 4, flexWrap: "wrap" }}>
                      <span style={{ fontSize: 12, color: "#6060aa" }}>{alarm.label || "No label"}</span>
                      <span style={{ color: "#333" }}>•</span>
                      <span style={{ fontSize: 11, color: "#5050aa" }}>
                        {alarm.days.length === 7 ? "Every day"
                          : alarm.days.length === 0 ? "No days"
                          : alarm.days.map(d => DAYS[d]).join(" ")}
                      </span>
                      {alarm.snoozeCount > 0 && (
                        <span style={{ fontSize: 10, background: "#1e1e3a", color: "#8080cc", padding: "1px 6px", borderRadius: 4 }}>
                          snoozed ×{alarm.snoozeCount}
                        </span>
                      )}
                    </div>
                  </div>
                  <div style={{ display: "flex", gap: 8, alignItems: "center" }}>
                    <button onClick={() => startEdit(alarm)} style={iconBtn}>✎</button>
                    <button onClick={() => deleteAlarm(alarm.id)} style={{ ...iconBtn, color: "#884444" }}>✕</button>
                    <Toggle checked={alarm.enabled} onChange={() => toggleAlarm(alarm.id)} />
                  </div>
                </div>
              )}
            </div>
          ))}

          {sortedAlarms.filter(a => !a._oneShot).length === 0 && !showAdd && (
            <div style={{ textAlign: "center", color: "#444", padding: "2rem", fontSize: 13, letterSpacing: 2 }}>
              NO ALARMS SET
            </div>
          )}
        </div>

        {/* Snooze info */}
        {sortedAlarms.filter(a => a._oneShot).length > 0 && (
          <div style={{ background: "#0e0e1e", border: "1px solid #2a2a3e", borderRadius: 10, padding: "0.8rem 1rem" }}>
            <div style={{ fontSize: 11, color: "#5060aa", letterSpacing: 2, marginBottom: 6 }}>SNOOZED</div>
            {sortedAlarms.filter(a => a._oneShot).map(a => (
              <div key={a.id} style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
                <span style={{ fontSize: 14, color: "#8888cc" }}>{a.label} → {formatTime12(a.hour, a.minute)}</span>
                <button onClick={() => deleteAlarm(a.id)} style={{ ...iconBtn, fontSize: 11, color: "#664444" }}>cancel</button>
              </div>
            ))}
          </div>
        )}

        <div style={{ textAlign: "center", marginTop: "2rem", fontSize: 10, color: "#2a2a4a", letterSpacing: 2 }}>
          SNOOZE = {SNOOZE_MINUTES} MIN • ALARM CLOCK
        </div>
      </div>
    </div>
  );
}

const iconBtn = {
  background: "transparent", border: "none", color: "#5050aa", cursor: "pointer",
  fontSize: 14, padding: "4px 6px", borderRadius: 6
};

function Toggle({ checked, onChange }) {
  return (
    <div onClick={onChange} style={{
      width: 44, height: 24, borderRadius: 12, cursor: "pointer",
      background: checked ? "#4040aa" : "#222", position: "relative", transition: "background 0.2s",
      border: `1px solid ${checked ? "#5050cc" : "#333"}`
    }}>
      <div style={{
        position: "absolute", top: 3, left: checked ? 22 : 3,
        width: 16, height: 16, borderRadius: 8, background: checked ? "#a0a0ff" : "#555",
        transition: "left 0.2s"
      }} />
    </div>
  );
}

function AlarmForm({ form, onChange, onSave, onCancel, saveLabel }) {
  const timeStr = `${pad(form.hour)}:${pad(form.minute)}`;

  function handleTime(val) {
    const { h, m } = parseTime(val);
    onChange(f => ({ ...f, hour: h, minute: m }));
  }

  function toggleDay(d) {
    onChange(f => ({
      ...f,
      days: f.days.includes(d) ? f.days.filter(x => x !== d) : [...f.days, d].sort()
    }));
  }

  return (
    <div>
      <div style={{ display: "flex", gap: 12, flexWrap: "wrap", marginBottom: 12 }}>
        <input type="time" value={timeStr} onChange={e => handleTime(e.target.value)} style={{
          background: "#0a0a14", border: "1px solid #2a2a4e", color: "#c0c0f0",
          borderRadius: 8, padding: "6px 10px", fontSize: 18, fontFamily: "monospace", letterSpacing: 2
        }} />
        <input type="text" placeholder="Label (optional)" value={form.label}
          onChange={e => onChange(f => ({ ...f, label: e.target.value }))} style={{
            background: "#0a0a14", border: "1px solid #2a2a4e", color: "#c0c0f0",
            borderRadius: 8, padding: "6px 10px", fontSize: 13, fontFamily: "monospace", flex: 1, minWidth: 120
          }} />
      </div>

      <div style={{ display: "flex", gap: 6, marginBottom: 12, flexWrap: "wrap" }}>
        {DAYS.map((d, i) => (
          <button key={i} onClick={() => toggleDay(i)} style={{
            padding: "4px 10px", borderRadius: 6, border: `1px solid ${form.days.includes(i) ? "#4040aa" : "#222"}`,
            background: form.days.includes(i) ? "#1e1e3e" : "#0a0a14",
            color: form.days.includes(i) ? "#a0a0ff" : "#555",
            cursor: "pointer", fontSize: 11, fontFamily: "monospace"
          }}>{d}</button>
        ))}
      </div>

      <div style={{ display: "flex", gap: 8, flexWrap: "wrap", marginBottom: 12 }}>
        {SOUNDS.map(s => (
          <button key={s.id} onClick={() => onChange(f => ({ ...f, sound: s.id }))} style={{
            padding: "4px 12px", borderRadius: 6, fontSize: 11, fontFamily: "monospace", cursor: "pointer",
            border: `1px solid ${form.sound === s.id ? "#4040aa" : "#222"}`,
            background: form.sound === s.id ? "#1e1e3e" : "#0a0a14",
            color: form.sound === s.id ? "#a0a0ff" : "#555"
          }}>{s.label}</button>
        ))}
      </div>

      <div style={{ display: "flex", gap: 10 }}>
        <button onClick={onSave} disabled={!form.days.length} style={{
          background: "#2a2a6e", border: "none", color: "#c0c0ff", padding: "8px 20px",
          borderRadius: 8, cursor: "pointer", fontSize: 12, fontFamily: "monospace", letterSpacing: 1
        }}>{saveLabel}</button>
        <button onClick={onCancel} style={{
          background: "transparent", border: "1px solid #2a2a3e", color: "#666",
          padding: "8px 16px", borderRadius: 8, cursor: "pointer", fontSize: 12, fontFamily: "monospace"
        }}>CANCEL</button>
      </div>
    </div>
  );
}