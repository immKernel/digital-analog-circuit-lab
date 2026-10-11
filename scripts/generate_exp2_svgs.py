# -*- coding: utf-8 -*-
import os

os.makedirs("images", exist_ok=True)

# 1. exp2_circuit_schematic.svg (单管低频放大电路原理图 图2-1)
exp2_fig1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 580" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .comp-label { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; font-weight: bold; fill: #0f172a; }
      .val-label { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 11px; fill: #475569; }
      .node-txt { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 12px; font-weight: bold; fill: #2563eb; }
      .dc-note { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 12px; fill: #b91c1c; }
      .ac-note { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 12px; fill: #047857; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="960" height="580" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />

  <text x="480" y="38" text-anchor="middle" class="title">图 2-1 单管低频共发射极电压放大实验电路图</text>
  <text x="480" y="60" text-anchor="middle" class="sub">三极管 3DG6 (NPN) · 阻容耦合 · 分压式偏置电位器调节静态工作点 Q</text>

  <!-- 主电路绘制区 -->
  <g transform="translate(60, 85)" filter="url(#shadow)">
    <rect width="840" height="420" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />

    <!-- 电源轨 +12V -->
    <line x1="260" y1="40" x2="680" y2="40" stroke="#dc2626" stroke-width="3" />
    <circle cx="680" cy="40" r="5" fill="#dc2626" />
    <text x="695" y="45" font-family="sans-serif" font-weight="bold" font-size="15" fill="#dc2626">Ec = +12V</text>

    <!-- 地线轨 GND -->
    <line x1="60" y1="360" x2="740" y2="360" stroke="#0f172a" stroke-width="3" />
    <!-- 接地符号 -->
    <path d="M 400 360 L 400 380 M 385 380 L 415 380 M 390 385 L 410 385 M 395 390 L 405 390" stroke="#0f172a" stroke-width="2" />
    <text x="400" y="405" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">GND (0V)</text>

    <!-- 1. 信号源与信号源内阻 Rs -->
    <!-- 信号源 us -->
    <circle cx="80" cy="240" r="18" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
    <path d="M 70 240 Q 75 233, 80 240 T 90 240" fill="none" stroke="#2563eb" stroke-width="2" />
    <text x="80" y="275" text-anchor="middle" class="comp-label">us</text>
    <line x1="80" y1="258" x2="80" y2="360" stroke="#0f172a" stroke-width="2" />
    <line x1="80" y1="222" x2="80" y2="200" stroke="#0f172a" stroke-width="2" />
    <line x1="80" y1="200" x2="130" y2="200" stroke="#0f172a" stroke-width="2" />

    <!-- 电阻 Rs = 10k -->
    <rect x="130" y="190" width="45" height="20" fill="#f1f5f9" stroke="#0f172a" stroke-width="2" />
    <text x="152" y="204" text-anchor="middle" font-size="10" font-weight="bold">10kΩ</text>
    <text x="152" y="180" text-anchor="middle" class="comp-label">Rs</text>
    <line x1="175" y1="200" x2="220" y2="200" stroke="#0f172a" stroke-width="2" />
    <circle cx="220" cy="200" r="4" fill="#2563eb" />
    <text x="220" y="185" text-anchor="middle" class="node-txt">ui</text>

    <!-- 输入耦合电容 C1 = 10uF -->
    <line x1="220" y1="200" x2="260" y2="200" stroke="#0f172a" stroke-width="2" />
    <!-- 电容符号极性 -->
    <line x1="260" y1="188" x2="260" y2="212" stroke="#0f172a" stroke-width="2.5" />
    <line x1="266" y1="188" x2="266" y2="212" stroke="#0f172a" stroke-width="2.5" />
    <text x="254" y="184" font-size="11" fill="#dc2626">+</text>
    <text x="263" y="175" text-anchor="middle" class="comp-label">C1</text>
    <text x="263" y="228" text-anchor="middle" class="val-label">10μF</text>
    <line x1="266" y1="200" x2="340" y2="200" stroke="#0f172a" stroke-width="2" />

    <!-- 2. 基极偏置回路：固定电阻 Rb' (50~200k) + 可调电位器 Rp (1~2M) -->
    <!-- 垂直回路从 Ec 经过 Rb' 和 Rp 到基极 -->
    <line x1="340" y1="40" x2="340" y2="80" stroke="#0f172a" stroke-width="2" />
    <rect x="330" y="80" width="20" height="40" fill="#f1f5f9" stroke="#0f172a" stroke-width="2" />
    <text x="360" y="98" class="comp-label">Rb'</text>
    <text x="360" y="112" class="val-label">50~200k</text>

    <line x1="340" y1="120" x2="340" y2="135" stroke="#0f172a" stroke-width="2" />
    <!-- 电位器 Rp -->
    <rect x="330" y="135" width="20" height="40" fill="#fef3c7" stroke="#d97706" stroke-width="2" />
    <!-- 调节箭头 -->
    <path d="M 315 160 L 355 145 M 355 145 L 348 144 M 355 145 L 354 152" stroke="#d97706" stroke-width="1.8" />
    <text x="360" y="152" class="comp-label" fill="#d97706">Rp</text>
    <text x="360" y="166" class="val-label">1~2MΩ</text>

    <line x1="340" y1="175" x2="340" y2="200" stroke="#0f172a" stroke-width="2" />
    <circle cx="340" cy="200" r="4" fill="#0f172a" />
    <text x="325" y="215" font-weight="bold" font-size="12" fill="#0f172a">B</text>

    <!-- 3. 晶体管 3DG6 (NPN) -->
    <circle cx="430" cy="200" r="32" fill="#f8fafc" stroke="#334155" stroke-width="2" />
    <!-- 基极连线与基区板 -->
    <line x1="340" y1="200" x2="415" y2="200" stroke="#0f172a" stroke-width="2" />
    <line x1="415" y1="182" x2="415" y2="218" stroke="#0f172a" stroke-width="3" />
    <!-- 集电极线 -->
    <line x1="415" y1="190" x2="445" y2="175" stroke="#0f172a" stroke-width="2" />
    <line x1="445" y1="175" x2="445" y2="140" stroke="#0f172a" stroke-width="2" />
    <text x="455" y="165" font-weight="bold" font-size="12" fill="#0f172a">C</text>
    <!-- 发射极线与箭头 (NPN 向外) -->
    <line x1="415" y1="210" x2="445" y2="225" stroke="#0f172a" stroke-width="2" />
    <polygon points="440,227 447,226 443,219" fill="#0f172a" />
    <line x1="445" y1="225" x2="445" y2="360" stroke="#0f172a" stroke-width="2" />
    <text x="455" y="240" font-weight="bold" font-size="12" fill="#0f172a">E</text>

    <text x="430" y="250" text-anchor="middle" font-size="11" font-weight="bold" fill="#3b82f6">3DG6 (NPN)</text>
    <text x="430" y="265" text-anchor="middle" font-size="10" fill="#64748b">β = 50~80</text>

    <!-- 4. 集电极负载电阻 Rc = 3k -->
    <line x1="445" y1="40" x2="445" y2="80" stroke="#0f172a" stroke-width="2" />
    <rect x="435" y="80" width="20" height="40" fill="#f1f5f9" stroke="#0f172a" stroke-width="2" />
    <text x="465" y="98" class="comp-label">Rc</text>
    <text x="465" y="112" class="val-label">3kΩ</text>
    <line x1="445" y1="120" x2="445" y2="140" stroke="#0f172a" stroke-width="2" />
    <circle cx="445" cy="140" r="4" fill="#0f172a" />

    <!-- 5. 输出耦合电容 C2 = 10uF -->
    <line x1="445" y1="140" x2="520" y2="140" stroke="#0f172a" stroke-width="2" />
    <line x1="520" y1="128" x2="520" y2="152" stroke="#0f172a" stroke-width="2.5" />
    <line x1="526" y1="128" x2="526" y2="152" stroke="#0f172a" stroke-width="2.5" />
    <text x="514" y="124" font-size="11" fill="#dc2626">+</text>
    <text x="523" y="115" text-anchor="middle" class="comp-label">C2</text>
    <text x="523" y="168" text-anchor="middle" class="val-label">10μF</text>
    <line x1="526" y1="140" x2="600" y2="140" stroke="#0f172a" stroke-width="2" />
    <circle cx="600" cy="140" r="4" fill="#0f172a" />

    <!-- 6. 负载电阻 RL = 3k -->
    <line x1="600" y1="140" x2="600" y2="210" stroke="#0f172a" stroke-width="2" />
    <rect x="590" y="210" width="20" height="40" fill="#f1f5f9" stroke="#0f172a" stroke-width="2" />
    <text x="620" y="228" class="comp-label">RL</text>
    <text x="620" y="242" class="val-label">3kΩ</text>
    <line x1="600" y1="250" x2="600" y2="360" stroke="#0f172a" stroke-width="2" />

    <!-- 输出端口 uo -->
    <line x1="600" y1="140" x2="680" y2="140" stroke="#0f172a" stroke-width="2" />
    <circle cx="680" cy="140" r="5" fill="#2563eb" />
    <text x="680" y="125" text-anchor="middle" class="node-txt">uo</text>
    <line x1="600" y1="360" x2="680" y2="360" stroke="#0f172a" stroke-width="2" />
    <circle cx="680" cy="360" r="5" fill="#2563eb" />

    <!-- 测量引线箭头 -->
    <path d="M 680 148 L 680 230 M 680 352 L 680 270" stroke="#2563eb" stroke-width="1.5" stroke-dasharray="3,3" />
    <circle cx="680" cy="250" r="16" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5" />
    <text x="680" y="255" text-anchor="middle" font-size="12" font-weight="bold" fill="#2563eb">uo</text>

    <!-- 右侧原理重点解说栏 -->
    <g transform="translate(640, 20)">
      <rect x="70" y="280" width="120" height="90" rx="6" fill="#f8fafc" stroke="#cbd5e1" />
      <text x="80" y="302" font-size="11" font-weight="bold" fill="#0f172a">核心测试要点：</text>
      <text x="80" y="322" font-size="10" fill="#475569">● 直流 Q 点：ui=0</text>
      <text x="80" y="340" font-size="10" fill="#475569">● 调 Rp 使 UC=6~8V</text>
      <text x="80" y="358" font-size="10" fill="#475569">● 交流放大：输入 1kHz</text>
    </g>
  </g>

  <!-- 底部关键原理提要 -->
  <rect x="60" y="515" width="840" height="50" rx="8" fill="#eff6ff" stroke="#bfdbfe" />
  <text x="80" y="535" font-family="sans-serif" font-weight="bold" font-size="12" fill="#1e40af">💡 调 Q 点物理链条：</text>
  <text x="80" y="552" font-family="sans-serif" font-size="11" fill="#1d4ed8">
    Rp 调大 ➔ 基极回路电阻 RB 变大 ➔ IB 变小 ➔ IC = β·IB 变小 ➔ 管压降 UCE = Ec - IC·Rc 升高（靠近电源 Ec，易产生截止失真）；反之 Rp 调小易产生饱和失真。
  </text>
</svg>'''

with open("images/exp2_circuit_schematic.svg", "w", encoding="utf-8") as f:
    f.write(exp2_fig1)

print("exp2_circuit_schematic generated")

# 2. exp2_h_equivalent_circuit.svg (微变等效电路与动态参数测量 图2-2, 2-3, 2-4)
exp2_fig2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 580" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .box-h { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 14px; font-weight: bold; fill: #1e293b; }
      .math { font-family: 'Consolas', monospace; font-size: 13px; font-weight: bold; fill: #0f172a; }
      .desc { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 11px; fill: #475569; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="980" height="580" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />

  <text x="490" y="38" text-anchor="middle" class="title">图 2-2 简化 h 微变等效电路与动态参数 (Au, Ri, Ro) 测量原理</text>
  <text x="490" y="60" text-anchor="middle" class="sub">三极管线性微变模型 · 放大倍数理论推导 · 输入/输出电阻等效测试法</text>

  <!-- 左侧：简化 h 微变等效电路 (图 2-2) -->
  <g transform="translate(40, 85)" filter="url(#shadow)">
    <rect width="440" height="290" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="30" class="box-h">图 2-2 简化 h 参数微变等效电路</text>

    <!-- 交流回路 -->
    <!-- 输入端 ui -->
    <circle cx="45" cy="110" r="4" fill="#2563eb" />
    <circle cx="45" cy="220" r="4" fill="#2563eb" />
    <text x="35" y="165" text-anchor="middle" font-weight="bold" fill="#2563eb" font-size="13">ui</text>
    <line x1="45" y1="110" x2="110" y2="110" stroke="#0f172a" stroke-width="2" />
    <line x1="45" y1="220" x2="400" y2="220" stroke="#0f172a" stroke-width="2" />

    <!-- 电阻 RB 支路 (可忽略或并联) -->
    <line x1="100" y1="110" x2="100" y2="140" stroke="#0f172a" stroke-width="2" />
    <rect x="92" y="140" width="16" height="35" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.8" />
    <text x="80" y="162" text-anchor="end" font-size="11" font-weight="bold">RB</text>
    <line x1="100" y1="175" x2="100" y2="220" stroke="#0f172a" stroke-width="2" />

    <!-- 输入回路 rbe -->
    <line x1="100" y1="110" x2="170" y2="110" stroke="#0f172a" stroke-width="2" />
    <line x1="170" y1="110" x2="170" y2="140" stroke="#0f172a" stroke-width="2" />
    <rect x="162" y="140" width="16" height="35" fill="#fef3c7" stroke="#d97706" stroke-width="2" />
    <text x="195" y="162" font-size="11" font-weight="bold" fill="#d97706">rbe</text>
    <line x1="170" y1="175" x2="170" y2="220" stroke="#0f172a" stroke-width="2" />

    <!-- 输入基极电流 Ib 标注 -->
    <path d="M 125 105 L 145 105 M 145 105 L 140 101 M 145 105 L 140 109" stroke="#2563eb" stroke-width="2" />
    <text x="135" y="98" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">ib</text>

    <!-- 受控电流源 β·ib (菱形符号) -->
    <g transform="translate(260, 160)">
      <polygon points="0,-22 18,0 0,22 -18,0" fill="#fee2e2" stroke="#dc2626" stroke-width="2" />
      <!-- 电流方向向下箭头 -->
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#dc2626" stroke-width="2" />
      <polygon points="0,14 -4,7 4,7" fill="#dc2626" />
      <text x="25" y="5" font-size="12" font-weight="bold" fill="#dc2626">β·ib</text>
    </g>
    <line x1="260" y1="110" x2="260" y2="138" stroke="#0f172a" stroke-width="2" />
    <line x1="260" y1="182" x2="260" y2="220" stroke="#0f172a" stroke-width="2" />

    <!-- 输出电阻 Rc -->
    <line x1="260" y1="110" x2="330" y2="110" stroke="#0f172a" stroke-width="2" />
    <line x1="330" y1="110" x2="330" y2="140" stroke="#0f172a" stroke-width="2" />
    <rect x="322" y="140" width="16" height="35" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.8" />
    <text x="312" y="162" text-anchor="end" font-size="11" font-weight="bold">Rc</text>
    <line x1="330" y1="175" x2="330" y2="220" stroke="#0f172a" stroke-width="2" />

    <!-- 负载电阻 RL -->
    <line x1="330" y1="110" x2="390" y2="110" stroke="#0f172a" stroke-width="2" />
    <line x1="390" y1="110" x2="390" y2="140" stroke="#0f172a" stroke-width="2" />
    <rect x="382" y="140" width="16" height="35" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.8" />
    <text x="412" y="162" font-size="11" font-weight="bold">RL</text>
    <line x1="390" y1="175" x2="390" y2="220" stroke="#0f172a" stroke-width="2" />

    <!-- 输出端 uo -->
    <circle cx="420" cy="110" r="4" fill="#2563eb" />
    <circle cx="420" cy="220" r="4" fill="#2563eb" />
    <line x1="390" y1="110" x2="420" y2="110" stroke="#0f172a" stroke-width="2" />
    <text x="420" y="165" text-anchor="middle" font-weight="bold" fill="#2563eb" font-size="13">uo</text>

    <!-- 公式说明 -->
    <rect x="20" y="235" width="400" height="42" rx="6" fill="#eff6ff" />
    <text x="30" y="254" class="math" fill="#1d4ed8">Au = uo / ui = - β · (Rc // RL) / rbe</text>
    <text x="30" y="270" class="desc">负号表示输出波形与输入波形反相 180°！</text>
  </g>

  <!-- 右侧：动态参数测量原理 (图 2-3 & 图 2-4) -->
  <g transform="translate(500, 85)" filter="url(#shadow)">
    <rect width="440" height="290" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" />
    <text x="20" y="30" class="box-h">动态参数等效测量原理</text>

    <!-- 输入电阻 Ri 测量 (图 2-3) -->
    <g transform="translate(20, 45)">
      <rect width="400" height="95" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
      <text x="15" y="22" font-size="12" font-weight="bold" fill="#0f172a">1. 输入电阻 Ri 测量原理（串联电阻比较法）：</text>
      <!-- 简易串联图 -->
      <circle cx="40" cy="55" r="12" fill="#eff6ff" stroke="#2563eb" />
      <text x="40" y="58" text-anchor="middle" font-size="9" font-weight="bold">us</text>
      <line x1="52" y1="55" x2="80" y2="55" stroke="#0f172a" stroke-width="1.5" />
      <rect x="80" y="48" width="30" height="14" fill="#ffffff" stroke="#0f172a" />
      <text x="95" y="59" text-anchor="middle" font-size="8">Rs</text>
      <line x1="110" y1="55" x2="140" y2="55" stroke="#0f172a" stroke-width="1.5" />
      <rect x="140" y="42" width="35" height="26" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5" />
      <text x="157" y="58" text-anchor="middle" font-size="10" font-weight="bold" fill="#2563eb">Ri</text>
      <line x1="40" y1="67" x2="40" y2="80" stroke="#0f172a" stroke-width="1.5" />
      <line x1="40" y1="80" x2="175" y2="80" stroke="#0f172a" stroke-width="1.5" />
      <line x1="157" y1="68" x2="157" y2="80" stroke="#0f172a" stroke-width="1.5" />
      
      <text x="200" y="52" class="math" fill="#b91c1c">Ri = [ui / (us - ui)] · Rs</text>
      <text x="200" y="72" class="desc">理论值：Ri = RB // rbe ≈ rbe</text>
    </g>

    <!-- 输出电阻 Ro 测量 (图 2-4) -->
    <g transform="translate(20, 155)">
      <rect width="400" height="115" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
      <text x="15" y="22" font-size="12" font-weight="bold" fill="#0f172a">2. 输出电阻 Ro 测量原理（带载/开路法）：</text>
      <!-- 简易戴维南等效图 -->
      <circle cx="40" cy="55" r="12" fill="#eff6ff" stroke="#2563eb" />
      <text x="40" y="58" text-anchor="middle" font-size="9" font-weight="bold">uo'</text>
      <line x1="52" y1="55" x2="80" y2="55" stroke="#0f172a" stroke-width="1.5" />
      <rect x="80" y="48" width="30" height="14" fill="#ffffff" stroke="#0f172a" />
      <text x="95" y="59" text-anchor="middle" font-size="8">Ro</text>
      <line x1="110" y1="55" x2="140" y2="55" stroke="#0f172a" stroke-width="1.5" />
      <rect x="140" y="48" width="30" height="14" fill="#fef3c7" stroke="#d97706" />
      <text x="155" y="59" text-anchor="middle" font-size="8">RL</text>
      <line x1="40" y1="67" x2="40" y2="80" stroke="#0f172a" stroke-width="1.5" />
      <line x1="40" y1="80" x2="155" y2="80" stroke="#0f172a" stroke-width="1.5" />
      <line x1="155" y1="62" x2="155" y2="80" stroke="#0f172a" stroke-width="1.5" />

      <text x="200" y="52" class="math" fill="#b91c1c">Ro = [(uo' - uo) / uo] · RL</text>
      <text x="200" y="72" class="desc">uo': 开路输出电压 (RL = ∞)</text>
      <text x="200" y="90" class="desc">uo: 接入 RL (3kΩ) 后的输出电压；理论值 Ro ≈ Rc</text>
    </g>
  </g>

  <!-- 底部理论核心计算公式看板 -->
  <g transform="translate(40, 395)">
    <rect width="900" height="160" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="url(#shadow)" />
    <text x="20" y="28" font-size="14" font-weight="bold" fill="#0f172a">📐 模电实验二 理论计算核心金公式：</text>

    <g transform="translate(20, 45)">
      <rect width="270" height="95" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
      <text x="15" y="25" font-size="12" font-weight="bold" fill="#1e40af">1. 晶体管输入电阻 rbe</text>
      <text x="15" y="50" class="math" font-size="12">rbe = 200Ω + (1+β)·(26mV / IE)</text>
      <text x="15" y="75" font-size="11" fill="#64748b">若 IE ≈ 1.5mA, β=60 ➔ rbe ≈ 1.25 kΩ</text>
    </g>

    <g transform="translate(310, 45)">
      <rect width="270" height="95" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
      <text x="15" y="25" font-size="12" font-weight="bold" fill="#047857">2. 电压放大倍数 Au</text>
      <text x="15" y="50" class="math" font-size="12">Au = - β · RL' / rbe</text>
      <text x="15" y="75" font-size="11" fill="#64748b">开路: RL'=Rc=3kΩ ➔ Au0 ≈ -144<br>带载: RL'=Rc//RL=1.5kΩ ➔ Au ≈ -72</text>
    </g>

    <g transform="translate(600, 45)">
      <rect width="280" height="95" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
      <text x="15" y="25" font-size="12" font-weight="bold" fill="#b45309">3. 静态工作点 Q 点估算</text>
      <text x="15" y="48" class="math" font-size="11">IB = (Ec - 0.7V) / RB</text>
      <text x="15" y="68" class="math" font-size="11">IC = β·IB,  UCE = Ec - IC·Rc</text>
      <text x="15" y="88" font-size="11" fill="#64748b">调试目标：UC = UCE ≈ 6V~8V</text>
    </g>
  </g>
</svg>'''

with open("images/exp2_h_equivalent_circuit.svg", "w", encoding="utf-8") as f:
    f.write(exp2_fig2)

print("exp2_h_equivalent_circuit generated")

# 3. exp2_distortion_analysis.svg (静态工作点对输出波形失真的影响分析)
exp2_fig3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 640" width="100%" height="100%">
  <defs>
    <style>
      .main-t { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .main-s { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .card-t { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 15px; font-weight: bold; }
      .txt { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 12px; fill: #334155; }
      .math { font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="1000" height="640" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />

  <text x="500" y="38" text-anchor="middle" class="main-t">图 2-3 静态工作点 (Q点) 对共射放大电路输出波形失真的影响机理</text>
  <text x="500" y="60" text-anchor="middle" class="main-s">饱和失真（削底） vs 截止失真（削顶）· NPN 与 PNP 对比 · 思考题 3 深度解答</text>

  <!-- 3 个失真状态卡片对比 -->

  <!-- 1. 饱和失真 (Q点过高) -->
  <g transform="translate(40, 85)" filter="url(#shadow)">
    <rect width="285" height="420" rx="12" fill="#ffffff" stroke="#fca5a5" stroke-width="2" />
    <rect x="15" y="15" width="255" height="130" rx="8" fill="#0f172a" />
    <!-- 示波器网格 -->
    <line x1="15" y1="80" x2="270" y2="80" stroke="#047857" stroke-dasharray="2,2" />
    <line x1="142" y1="15" x2="142" y2="145" stroke="#047857" stroke-dasharray="2,2" />
    
    <!-- 饱和失真波形 (NPN共射：底部削平！) -->
    <!-- 正半周圆滑，负半周底部削平一条水平线 -->
    <path d="M 30 80 Q 55 25, 80 80 L 95 115 L 125 115 L 140 80 Q 165 25, 190 80 L 205 115 L 235 115 L 250 80" 
          fill="none" stroke="#ef4444" stroke-width="2.5" />
    <line x1="90" y1="115" x2="130" y2="115" stroke="#fbbf24" stroke-width="3" stroke-dasharray="3,2" />
    <text x="142" y="132" text-anchor="middle" font-size="10" font-weight="bold" fill="#f87171">底部被削平 (饱和失真)</text>

    <text x="15" y="170" class="card-t" fill="#b91c1c">❌ 饱和失真 (Q 点过高)</text>
    <text x="15" y="195" class="txt"><tspan font-weight="bold">产生原因：</tspan> Rp 调得太小 ➔ IB、IC 过大</text>
    <text x="15" y="215" class="txt"><tspan font-weight="bold">静态状态：</tspan> UCE 过低 (靠近 0V，UC &lt; 3V)</text>
    <text x="15" y="235" class="txt"><tspan font-weight="bold">物理机制：</tspan> 输入正半周时晶体管进入饱和区，UCE 下降到饱和压降 UCES 无法再降低。</text>
    <text x="15" y="265" class="txt" fill="#b91c1c"><tspan font-weight="bold">波形表现（NPN）：</tspan><br>因共射放大有 180° 反相，输入正半周对应输出负半周，因此<tspan font-weight="bold" fill="#dc2626">输出波形下半部（底部）削平</tspan>！</text>
    
    <rect x="15" y="325" width="255" height="75" rx="6" fill="#fef2f2" stroke="#fecaca" />
    <text x="25" y="348" font-size="11" font-weight="bold" fill="#991b1b">💡 排除调节手段：</text>
    <text x="25" y="368" font-size="10" fill="#7f1d1d">顺时针调大 Rp 阻值 ➔ 减小基极电流 IB ➔ 提高集电极直流电位 UC 到 6~8V。</text>
  </g>

  <!-- 2. 正常工作 (Q点适中，最大不失真) -->
  <g transform="translate(355, 85)" filter="url(#shadow)">
    <rect width="285" height="420" rx="12" fill="#ffffff" stroke="#86efac" stroke-width="2" />
    <rect x="15" y="15" width="255" height="130" rx="8" fill="#064e3b" />
    <line x1="15" y1="80" x2="270" y2="80" stroke="#047857" stroke-width="1.5" stroke-dasharray="2,2" />
    <line x1="142" y1="15" x2="142" y2="145" stroke="#047857" stroke-width="1.5" stroke-dasharray="2,2" />
    
    <!-- 完美对称正弦波 -->
    <path d="M 30 80 Q 55 30, 80 80 T 130 80 T 180 80 T 230 80" 
          fill="none" stroke="#34d399" stroke-width="2.5" />
    <text x="142" y="132" text-anchor="middle" font-size="10" font-weight="bold" fill="#34d399">上下完全对称 (无失真)</text>

    <text x="15" y="170" class="card-t" fill="#047857">✨ 最佳状态 (Q 点适中)</text>
    <text x="15" y="195" class="txt"><tspan font-weight="bold">静态目标：</tspan> UCE ≈ Ec / 2 ≈ 6V ~ 8V</text>
    <text x="15" y="215" class="txt"><tspan font-weight="bold">动态特性：</tspan> 位于交流负载线正中心</text>
    <text x="15" y="235" class="txt"><tspan font-weight="bold">物理机制：</tspan> 向上摆动与向下摆动均拥有最大余量，动态范围最宽。</text>
    <text x="15" y="265" class="txt" fill="#047857"><tspan font-weight="bold">输出特征：</tspan><br>正弦波上下半周光滑对称，电压放大倍数稳定达到 -60 ~ -80 左右。</text>

    <rect x="15" y="325" width="255" height="75" rx="6" fill="#ecfdf5" stroke="#a7f3d0" />
    <text x="25" y="348" font-size="11" font-weight="bold" fill="#065f46">🏆 实验操作规范：</text>
    <text x="25" y="368" font-size="10" fill="#047857">做动态测试前，必须严格先微调 Rp 使 UC=6~8V，再加输入交流信号！</text>
  </g>

  <!-- 3. 截止失真 (Q点过低) -->
  <g transform="translate(670, 85)" filter="url(#shadow)">
    <rect width="285" height="420" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" />
    <rect x="15" y="15" width="255" height="130" rx="8" fill="#0f172a" />
    <line x1="15" y1="80" x2="270" y2="80" stroke="#047857" stroke-dasharray="2,2" />
    <line x1="142" y1="15" x2="142" y2="145" stroke="#047857" stroke-dasharray="2,2" />
    
    <!-- 截止失真波形 (NPN共射：顶部削平！) -->
    <path d="M 30 80 L 45 45 L 75 45 L 90 80 Q 115 130, 140 80 L 155 45 L 185 45 L 200 80 Q 225 130, 250 80" 
          fill="none" stroke="#f59e0b" stroke-width="2.5" />
    <line x1="45" y1="45" x2="75" y2="45" stroke="#ef4444" stroke-width="3" stroke-dasharray="3,2" />
    <text x="142" y="132" text-anchor="middle" font-size="10" font-weight="bold" fill="#fcd34d">顶部被削平 (截止失真)</text>

    <text x="15" y="170" class="card-t" fill="#d97706">⚠️ 截止失真 (Q 点过低)</text>
    <text x="15" y="195" class="txt"><tspan font-weight="bold">产生原因：</tspan> Rp 调得太大 ➔ IB、IC 过小</text>
    <text x="15" y="215" class="txt"><tspan font-weight="bold">静态状态：</tspan> UCE 过高 (接近 Ec，UC &gt; 10V)</text>
    <text x="15" y="235" class="txt"><tspan font-weight="bold">物理机制：</tspan> 输入负半周时发射结反偏截止，集电极电流 iC = 0，输出电位被钳位在 Ec。</text>
    <text x="15" y="265" class="txt" fill="#d97706"><tspan font-weight="bold">波形表现（NPN）：</tspan><br>反相放大使得输入负半周对应输出正半周，因此<tspan font-weight="bold" fill="#b45309">输出波形上半部（顶部）削平</tspan>！</text>

    <rect x="15" y="325" width="255" height="75" rx="6" fill="#fffbeb" stroke="#fde68a" />
    <text x="25" y="348" font-size="11" font-weight="bold" fill="#92400e">💡 排除调节手段：</text>
    <text x="25" y="368" font-size="10" fill="#78350f">逆时针调小 Rp 阻值 ➔ 增大基极电流 IB ➔ 降低集电极直流电位 UC 到 6~8V。</text>
  </g>

  <!-- 底部思考题 3 专题解答框 (NPN vs PNP 极性反转) -->
  <g transform="translate(40, 520)">
    <rect width="915" height="100" rx="10" fill="#eff6ff" stroke="#93c5fd" stroke-width="1.5" />
    <text x="20" y="28" font-size="13" font-weight="bold" fill="#1e3a8a">🔥 课后思考题 3 深度辨析：若采用 PNP 型三极管，失真情况如何？</text>
    <text x="20" y="52" font-size="12" fill="#1e40af">
      ● <tspan font-weight="bold">NPN 型三极管：</tspan> 饱和失真对应输出波形 <tspan font-weight="bold" fill="#dc2626">下部削平（削底）</tspan>；截止失真对应输出波形 <tspan font-weight="bold" fill="#d97706">上部削平（削顶）</tspan>。
    </text>
    <text x="20" y="74" font-size="12" fill="#1e40af">
      ● <tspan font-weight="bold">PNP 型三极管：</tspan> 由于电源极性为负电源且导通方向相反，共射放大时输出相位发生极性倒置：<br>
      &nbsp;&nbsp;&nbsp;&nbsp;饱和失真变为 <tspan font-weight="bold" fill="#dc2626">上部削平（削顶）</tspan>；截止失真变为 <tspan font-weight="bold" fill="#d97706">下部削平（削底）</tspan>！两者正好完全颠倒！
    </text>
  </g>
</svg>'''

with open("images/exp2_distortion_analysis.svg", "w", encoding="utf-8") as f:
    f.write(exp2_fig3)

print("exp2_distortion_analysis generated")

# 4. exp2_dynamic_measurement_flow.svg (动态参数测试流程与实操规范)
exp2_fig4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 500" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .step-t { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 14px; font-weight: bold; fill: #0f172a; }
      .step-c { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 11px; fill: #475569; }
      .num { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; font-weight: bold; fill: #ffffff; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="980" height="500" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />

  <text x="490" y="38" text-anchor="middle" class="title">图 2-4 模电实验二 规范化动态参数测试 SOP 流程全景图</text>
  <text x="490" y="60" text-anchor="middle" class="sub">从静态调零到动态测幅、阻抗测定、失真观察的五步标准实验路径</text>

  <!-- 5 个步骤卡片横向流转 -->
  <!-- 宽 165, 间距 18, x起始 40 -->

  <!-- 步骤 1 -->
  <g transform="translate(40, 85)" filter="url(#shadow)">
    <rect width="168" height="280" rx="10" fill="#ffffff" stroke="#93c5fd" stroke-width="1.8" />
    <circle cx="32" cy="30" r="14" fill="#2563eb" />
    <text x="32" y="35" text-anchor="middle" class="num">1</text>
    <text x="55" y="35" class="step-t">调静态工作点</text>
    
    <text x="15" y="75" class="step-c">● <tspan font-weight="bold">断开输入信号</tspan> (ui = 0)</text>
    <text x="15" y="98" class="step-c">● 接通 +12V 直流电源</text>
    <text x="15" y="121" class="step-c">● 用万用表测集电极电位 UC</text>
    <text x="15" y="144" class="step-c">● 细调电位器 Rp 使：<br>&nbsp;&nbsp;<tspan font-weight="bold" fill="#dc2626">UC = 6.0 ~ 8.0 V</tspan></text>
    <text x="15" y="185" class="step-c">● 测出 UB, UE, UBE, UCE</text>
    <text x="15" y="208" class="step-c">● 断电拆测 RB 阻值</text>
    <text x="15" y="235" font-size="11" font-weight="bold" fill="#2563eb">完成表 2-1 记录</text>
  </g>

  <!-- 步骤 2 -->
  <g transform="translate(225, 85)" filter="url(#shadow)">
    <rect width="168" height="280" rx="10" fill="#ffffff" stroke="#93c5fd" stroke-width="1.8" />
    <circle cx="32" cy="30" r="14" fill="#2563eb" />
    <text x="32" y="35" text-anchor="middle" class="num">2</text>
    <text x="55" y="35" class="step-t">接入正弦激励</text>
    
    <text x="15" y="75" class="step-c">● 信号源置于正弦波</text>
    <text x="15" y="98" class="step-c">● 设定频率 <tspan font-weight="bold">f = 1 kHz</tspan></text>
    <text x="15" y="121" class="step-c">● 调节信号源幅度微调</text>
    <text x="15" y="144" class="step-c">● 示波器监视输出 uo</text>
    <text x="15" y="167" class="step-c">● 确保波形完全不失真</text>
    <text x="15" y="195" class="step-c">● 将毫伏表探头接 ui 端</text>
    <text x="15" y="218" class="step-c">● 调定 ui = 5 ~ 10 mV</text>
    <text x="15" y="245" font-size="11" font-weight="bold" fill="#2563eb">确保小信号线性放大</text>
  </g>

  <!-- 步骤 3 -->
  <g transform="translate(410, 85)" filter="url(#shadow)">
    <rect width="168" height="280" rx="10" fill="#ffffff" stroke="#93c5fd" stroke-width="1.8" />
    <circle cx="32" cy="30" r="14" fill="#2563eb" />
    <text x="32" y="35" text-anchor="middle" class="num">3</text>
    <text x="55" y="35" class="step-t">测增益与阻抗</text>
    
    <text x="15" y="75" class="step-c">● <tspan font-weight="bold">测 Au：</tspan>毫伏表测 ui 与 uo</text>
    <text x="15" y="98" class="step-c">● 断开 RL 测得空载 uo'</text>
    <text x="15" y="121" class="step-c">● 接上 RL 测得带载 uo</text>
    <text x="15" y="148" class="step-c">● <tspan font-weight="bold">测 Ri：</tspan>测 us 与 ui</text>
    <text x="15" y="171" class="step-c">计算 Ri = [ui/(us-ui)]·Rs</text>
    <text x="15" y="200" class="step-c">● <tspan font-weight="bold">测 Ro：</tspan>代入公式</text>
    <text x="15" y="223" class="step-c">Ro = [(uo'-uo)/uo]·RL</text>
    <text x="15" y="250" font-size="11" font-weight="bold" fill="#2563eb">完成表 2-2 ~ 2-4</text>
  </g>

  <!-- 步骤 4 -->
  <g transform="translate(595, 85)" filter="url(#shadow)">
    <rect width="168" height="280" rx="10" fill="#ffffff" stroke="#fca5a5" stroke-width="1.8" />
    <circle cx="32" cy="30" r="14" fill="#dc2626" />
    <text x="32" y="35" text-anchor="middle" class="num">4</text>
    <text x="55" y="35" class="step-t">失真特征观测</text>
    
    <text x="15" y="75" class="step-c">● 将 Rs 短路加大输入信号</text>
    <text x="15" y="98" class="step-c">● 使 ui 升至 20~40 mV</text>
    <text x="15" y="125" class="step-c">● <tspan font-weight="bold">调 Rp 最小：</tspan>记录波形及 UB, UC（底部削平-饱和）</text>
    <text x="15" y="165" class="step-c">● <tspan font-weight="bold">调 Rp 最大：</tspan>记录波形及 UB, UC（顶部削平-截止）</text>
    <text x="15" y="205" class="step-c">● 恢复正常并测静点对 Au 影响（UC=9V vs 7.5V）</text>
    <text x="15" y="245" font-size="11" font-weight="bold" fill="#dc2626">完成表 2-5 &amp; 2-6</text>
  </g>

  <!-- 步骤 5 -->
  <g transform="translate(780, 85)" filter="url(#shadow)">
    <rect width="160" height="280" rx="10" fill="#ffffff" stroke="#86efac" stroke-width="1.8" />
    <circle cx="32" cy="30" r="14" fill="#16a34a" />
    <text x="32" y="35" text-anchor="middle" class="num">5</text>
    <text x="55" y="35" class="step-t">最大不失真幅度</text>
    
    <text x="15" y="75" class="step-c">● 将 Q 点恢复至中央</text>
    <text x="15" y="98" class="step-c">● 缓慢逐次增大信号源 ui</text>
    <text x="15" y="125" class="step-c">● 示波器严密监测波形</text>
    <text x="15" y="152" class="step-c">● 寻找<tspan font-weight="bold" fill="#059669">临界失真点</tspan>（上下峰值即将削平前瞬间）</text>
    <text x="15" y="195" class="step-c">● 毫伏表读取此时电压</text>
    <text x="15" y="218" class="step-c">● 记下最大输出 Uomax</text>
    <text x="15" y="245" font-size="11" font-weight="bold" fill="#16a34a">收工整理数据与关机</text>
  </g>

  <!-- 底部强调规范 -->
  <g transform="translate(40, 390)">
    <rect width="900" height="80" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
    <text x="25" y="30" font-size="13" font-weight="bold" fill="#0f172a">⚠️ 动态测试三大实操铁律：</text>
    <text x="25" y="52" font-size="12" fill="#334155">
      1. 测电压放大倍数时，示波器与毫伏表必须同时并联在输出端（示波器看波形是否失真，毫伏表读有效值，二者缺一不可！）。<br>
      2. 测输入电阻 Ri 时，注意区分信号源开路端电压 us 与放大电路输入端电压 ui（二者相差在内阻 Rs 上的压降）。
    </text>
  </g>
</svg>'''

with open("images/exp2_dynamic_measurement_flow.svg", "w", encoding="utf-8") as f:
    f.write(exp2_fig4)

print("exp2_dynamic_measurement_flow generated")

# 5. exp2_troubleshooting_qpoint.svg (故障排查与思考题2: UC ≈ Ec 故障树)
exp2_fig5 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .node-t { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; font-weight: bold; }
      .txt { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 11px; fill: #475569; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="960" height="480" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />

  <text x="480" y="38" text-anchor="middle" class="title">图 2-5 模电实验二 故障树排查图（重点攻关思考题 2：UC ≈ Ec 根源分析）</text>
  <text x="480" y="60" text-anchor="middle" class="sub">深入剖析集电极直流电位异常高达 +12V 的物理成因、检查顺序与排除方案</text>

  <!-- 故障源头根节点 -->
  <g transform="translate(330, 85)" filter="url(#shadow)">
    <rect width="300" height="65" rx="10" fill="#fef2f2" stroke="#ef4444" stroke-width="2" />
    <text x="150" y="28" text-anchor="middle" class="node-t" fill="#991b1b">故障现象：测静态工作点时 UC ≈ Ec (+12V)</text>
    <text x="150" y="48" text-anchor="middle" font-size="12" fill="#b91c1c" font-weight="bold">本质原因：集电极电流 IC = 0，无任何压降 (URc = 0)</text>
  </g>

  <!-- 3 条排查分支 -->
  <!-- 分支连线 -->
  <path d="M 480 150 L 480 175 M 480 175 L 180 175 L 180 200 M 480 175 L 480 200 M 480 175 L 780 175 L 780 200" 
        fill="none" stroke="#64748b" stroke-width="2" />

  <!-- 分支 1：基极偏置开路 -->
  <g transform="translate(60, 200)" filter="url(#shadow)">
    <rect width="250" height="175" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
    <rect x="12" y="12" width="6" height="18" rx="3" fill="#ef4444" />
    <text x="24" y="26" class="node-t" fill="#1e293b">可能原因 ①：基极回路开路</text>
    <text x="15" y="55" class="txt">● <tspan font-weight="bold">偏置电阻断路：</tspan>固定电阻 Rb' 虚焊或烧断；</text>
    <text x="15" y="75" class="txt">● <tspan font-weight="bold">电位器触点脱落：</tspan>Rp 碳膜断路或调到断开点；</text>
    <text x="15" y="95" class="txt">● <tspan font-weight="bold">连接线虚接：</tspan>从电源 Ec 到基极 B 间的跳线脱落。</text>
    <rect x="12" y="115" width="226" height="45" rx="6" fill="#f8fafc" stroke="#e2e8f0" />
    <text x="20" y="132" font-size="11" font-weight="bold" fill="#0f172a">🔍 诊断手段：</text>
    <text x="20" y="148" font-size="10" fill="#b91c1c">测 UB，若 UB = 0V 说明基极无偏置！</text>
  </g>

  <!-- 分支 2：三极管损坏失效 -->
  <g transform="translate(355, 200)" filter="url(#shadow)">
    <rect width="250" height="175" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
    <rect x="12" y="12" width="6" height="18" rx="3" fill="#d97706" />
    <text x="24" y="26" class="node-t" fill="#1e293b">可能原因 ②：晶体管本身损坏</text>
    <text x="15" y="55" class="txt">● <tspan font-weight="bold">发射结开路：</tspan>内部发射结烧断，无法注入载流子；</text>
    <text x="15" y="75" class="txt">● <tspan font-weight="bold">集电结断路：</tspan>导致集电极电流无法流通；</text>
    <text x="15" y="95" class="txt">● <tspan font-weight="bold">管脚插错：</tspan>b、c、e 管脚颠倒，三极管截止。</text>
    <rect x="12" y="115" width="226" height="45" rx="6" fill="#f8fafc" stroke="#e2e8f0" />
    <text x="20" y="132" font-size="11" font-weight="bold" fill="#0f172a">🔍 诊断手段：</text>
    <text x="20" y="148" font-size="10" fill="#d97706">万用表拔出测二极管档/hFE，更换3DG6！</text>
  </g>

  <!-- 分支 3：发射极未接地 -->
  <g transform="translate(650, 200)" filter="url(#shadow)">
    <rect width="250" height="175" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
    <rect x="12" y="12" width="6" height="18" rx="3" fill="#2563eb" />
    <text x="24" y="26" class="node-t" fill="#1e293b">可能原因 ③：发射极回路不通</text>
    <text x="15" y="55" class="txt">● <tspan font-weight="bold">地线悬空：</tspan>发射极 e 未连接至公共接地端 GND；</text>
    <text x="15" y="75" class="txt">● <tspan font-weight="bold">插孔接触不良：</tspan>实验箱插孔弹性疲劳失效；</text>
    <text x="15" y="95" class="txt">● <tspan font-weight="bold">集电极负载短路：</tspan>Rc 阻值为 0（极少见）。</text>
    <rect x="12" y="115" width="226" height="45" rx="6" fill="#f8fafc" stroke="#e2e8f0" />
    <text x="20" y="132" font-size="11" font-weight="bold" fill="#0f172a">🔍 诊断手段：</text>
    <text x="20" y="148" font-size="10" fill="#2563eb">测 UE，若 UE 异常偏高或浮空说明未接地！</text>
  </g>

  <!-- 底部思考题 1 顺带总结 -->
  <g transform="translate(60, 395)">
    <rect width="840" height="65" rx="8" fill="#ecfdf5" stroke="#a7f3d0" />
    <text x="20" y="26" font-size="12" font-weight="bold" fill="#065f46">💡 思考题 1 顺带攻关：RB 不拔下来直接在电路中测量可以吗？</text>
    <text x="20" y="46" font-size="11" fill="#047857">
      不可以！若直接在线测量，三极管发射结的等效电阻与电源内阻会并联在测量表笔两端，导致读数严重偏小；且带电测量会烧毁万用表电阻档！必须断电并断开相关引脚后测量。
    </text>
  </g>
</svg>'''

with open("images/exp2_troubleshooting_qpoint.svg", "w", encoding="utf-8") as f:
    f.write(exp2_fig5)

print("exp2_troubleshooting_qpoint generated")
