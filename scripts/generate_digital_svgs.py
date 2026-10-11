# -*- coding: utf-8 -*-
import os

os.makedirs("images", exist_ok=True)

# 1. exp_dig1_gate_pinouts.svg (74LS20, 74LS00, 74LS04, 74LS125 管脚排列图及内部逻辑)
dig1_fig1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 580" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .chip-t { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 15px; font-weight: bold; fill: #1e3a8a; }
      .pin-num { font-family: 'Consolas', monospace; font-size: 11px; font-weight: bold; fill: #334155; }
      .pin-name { font-family: 'Consolas', monospace; font-size: 11px; font-weight: bold; fill: #0f172a; }
      .gate-txt { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 11px; fill: #475569; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="980" height="580" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />

  <text x="490" y="38" text-anchor="middle" class="title">图 1-1 实验一 常用数字集成门电路引脚排列与逻辑符号 (DIP-14 封装)</text>
  <text x="490" y="60" text-anchor="middle" class="sub">74LS20 (双4输入与非) · 74LS00 (四2输入与非) · 74LS04 (六反相器) · 74LS125 (四三态缓冲门)</text>

  <!-- 4 个芯片并排，每个宽 210, 间距 20, x 起始 45 -->

  <!-- 1. 74LS20 -->
  <g transform="translate(45, 85)" filter="url(#shadow)">
    <rect width="210" height="400" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="105" y="30" text-anchor="middle" class="chip-t">74LS20</text>
    <text x="105" y="48" text-anchor="middle" class="gate-txt">双 4 输入与非门</text>

    <!-- 芯片本体外壳 -->
    <rect x="55" y="65" width="100" height="260" rx="6" fill="#1e293b" />
    <!-- 缺口 notch -->
    <path d="M 95 65 A 10 10 0 0 0 115 65" fill="#ffffff" />
    
    <!-- 左侧引脚 1~7 -->
    <!-- y 步长: 32px -->
    <!-- Pin 1 -->
    <line x1="25" y1="85" x2="55" y2="85" stroke="#64748b" stroke-width="3" />
    <text x="18" y="89" text-anchor="end" class="pin-name">1A</text><text x="63" y="89" class="pin-num" fill="#fff">1</text>
    <!-- Pin 2 -->
    <line x1="25" y1="120" x2="55" y2="120" stroke="#64748b" stroke-width="3" />
    <text x="18" y="124" text-anchor="end" class="pin-name">1B</text><text x="63" y="124" class="pin-num" fill="#fff">2</text>
    <!-- Pin 3 -->
    <line x1="25" y1="155" x2="55" y2="155" stroke="#94a3b8" stroke-width="2" />
    <text x="18" y="159" text-anchor="end" class="pin-name" fill="#94a3b8">NC</text><text x="63" y="159" class="pin-num" fill="#fff">3</text>
    <!-- Pin 4 -->
    <line x1="25" y1="190" x2="55" y2="190" stroke="#64748b" stroke-width="3" />
    <text x="18" y="194" text-anchor="end" class="pin-name">1C</text><text x="63" y="194" class="pin-num" fill="#fff">4</text>
    <!-- Pin 5 -->
    <line x1="25" y1="225" x2="55" y2="225" stroke="#64748b" stroke-width="3" />
    <text x="18" y="229" text-anchor="end" class="pin-name">1D</text><text x="63" y="229" class="pin-num" fill="#fff">5</text>
    <!-- Pin 6 -->
    <line x1="25" y1="260" x2="55" y2="260" stroke="#2563eb" stroke-width="3" />
    <text x="18" y="264" text-anchor="end" class="pin-name" fill="#2563eb">1Y</text><text x="63" y="264" class="pin-num" fill="#fff">6</text>
    <!-- Pin 7: GND -->
    <line x1="25" y1="295" x2="55" y2="295" stroke="#0f172a" stroke-width="3" />
    <text x="18" y="299" text-anchor="end" class="pin-name">GND</text><text x="63" y="299" class="pin-num" fill="#fff">7</text>

    <!-- 右侧引脚 8~14 (从下到上) -->
    <!-- Pin 8: 2Y -->
    <line x1="155" y1="295" x2="185" y2="295" stroke="#2563eb" stroke-width="3" />
    <text x="192" y="299" class="pin-name" fill="#2563eb">2Y</text><text x="142" y="299" class="pin-num" fill="#fff">8</text>
    <!-- Pin 9: 2A -->
    <line x1="155" y1="260" x2="185" y2="260" stroke="#64748b" stroke-width="3" />
    <text x="192" y="264" class="pin-name">2A</text><text x="142" y="264" class="pin-num" fill="#fff">9</text>
    <!-- Pin 10: 2B -->
    <line x1="155" y1="225" x2="185" y2="225" stroke="#64748b" stroke-width="3" />
    <text x="192" y="229" class="pin-name">2B</text><text x="138" y="229" class="pin-num" fill="#fff">10</text>
    <!-- Pin 11: NC -->
    <line x1="155" y1="190" x2="185" y2="190" stroke="#94a3b8" stroke-width="2" />
    <text x="192" y="194" class="pin-name" fill="#94a3b8">NC</text><text x="138" y="194" class="pin-num" fill="#fff">11</text>
    <!-- Pin 12: 2C -->
    <line x1="155" y1="155" x2="185" y2="155" stroke="#64748b" stroke-width="3" />
    <text x="192" y="159" class="pin-name">2C</text><text x="138" y="159" class="pin-num" fill="#fff">12</text>
    <!-- Pin 13: 2D -->
    <line x1="155" y1="120" x2="185" y2="120" stroke="#64748b" stroke-width="3" />
    <text x="192" y="124" class="pin-name">2D</text><text x="138" y="124" class="pin-num" fill="#fff">13</text>
    <!-- Pin 14: Vcc -->
    <line x1="155" y1="85" x2="185" y2="85" stroke="#dc2626" stroke-width="3" />
    <text x="192" y="89" class="pin-name" fill="#dc2626">Vcc</text><text x="138" y="89" class="pin-num" fill="#fff">14</text>

    <!-- 底部逻辑函数 -->
    <rect x="15" y="340" width="180" height="45" rx="6" fill="#f8fafc" stroke="#e2e8f0" />
    <text x="105" y="367" text-anchor="middle" font-family="Consolas" font-weight="bold" font-size="12" fill="#1e40af">Y = !(A·B·C·D)</text>
  </g>

  <!-- 2. 74LS00 -->
  <g transform="translate(275, 85)" filter="url(#shadow)">
    <rect width="210" height="400" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="105" y="30" text-anchor="middle" class="chip-t">74LS00</text>
    <text x="105" y="48" text-anchor="middle" class="gate-txt">四 2 输入与非门</text>

    <rect x="55" y="65" width="100" height="260" rx="6" fill="#1e293b" />
    <path d="M 95 65 A 10 10 0 0 0 115 65" fill="#ffffff" />

    <!-- 1A, 1B, 1Y, 2A, 2B, 2Y, GND -->
    <line x1="25" y1="85" x2="55" y2="85" stroke="#64748b" stroke-width="3" /><text x="18" y="89" text-anchor="end" class="pin-name">1A</text><text x="63" y="89" class="pin-num" fill="#fff">1</text>
    <line x1="25" y1="120" x2="55" y2="120" stroke="#64748b" stroke-width="3" /><text x="18" y="124" text-anchor="end" class="pin-name">1B</text><text x="63" y="124" class="pin-num" fill="#fff">2</text>
    <line x1="25" y1="155" x2="55" y2="155" stroke="#2563eb" stroke-width="3" /><text x="18" y="159" text-anchor="end" class="pin-name" fill="#2563eb">1Y</text><text x="63" y="159" class="pin-num" fill="#fff">3</text>
    <line x1="25" y1="190" x2="55" y2="190" stroke="#64748b" stroke-width="3" /><text x="18" y="194" text-anchor="end" class="pin-name">2A</text><text x="63" y="194" class="pin-num" fill="#fff">4</text>
    <line x1="25" y1="225" x2="55" y2="225" stroke="#64748b" stroke-width="3" /><text x="18" y="229" text-anchor="end" class="pin-name">2B</text><text x="63" y="229" class="pin-num" fill="#fff">5</text>
    <line x1="25" y1="260" x2="55" y2="260" stroke="#2563eb" stroke-width="3" /><text x="18" y="264" text-anchor="end" class="pin-name" fill="#2563eb">2Y</text><text x="63" y="264" class="pin-num" fill="#fff">6</text>
    <line x1="25" y1="295" x2="55" y2="295" stroke="#0f172a" stroke-width="3" /><text x="18" y="299" text-anchor="end" class="pin-name">GND</text><text x="63" y="299" class="pin-num" fill="#fff">7</text>

    <!-- 右侧: 3Y, 3A, 3B, 4Y, 4A, 4B, Vcc -->
    <line x1="155" y1="295" x2="185" y2="295" stroke="#2563eb" stroke-width="3" /><text x="192" y="299" class="pin-name" fill="#2563eb">3Y</text><text x="142" y="299" class="pin-num" fill="#fff">8</text>
    <line x1="155" y1="260" x2="185" y2="260" stroke="#64748b" stroke-width="3" /><text x="192" y="264" class="pin-name">3A</text><text x="142" y="264" class="pin-num" fill="#fff">9</text>
    <line x1="155" y1="225" x2="185" y2="225" stroke="#64748b" stroke-width="3" /><text x="192" y="229" class="pin-name">3B</text><text x="138" y="229" class="pin-num" fill="#fff">10</text>
    <line x1="155" y1="190" x2="185" y2="190" stroke="#2563eb" stroke-width="3" /><text x="192" y="194" class="pin-name" fill="#2563eb">4Y</text><text x="138" y="194" class="pin-num" fill="#fff">11</text>
    <line x1="155" y1="155" x2="185" y2="155" stroke="#64748b" stroke-width="3" /><text x="192" y="159" class="pin-name">4A</text><text x="138" y="159" class="pin-num" fill="#fff">12</text>
    <line x1="155" y1="120" x2="185" y2="120" stroke="#64748b" stroke-width="3" /><text x="192" y="124" class="pin-name">4B</text><text x="138" y="124" class="pin-num" fill="#fff">13</text>
    <line x1="155" y1="85" x2="185" y2="85" stroke="#dc2626" stroke-width="3" /><text x="192" y="89" class="pin-name" fill="#dc2626">Vcc</text><text x="138" y="89" class="pin-num" fill="#fff">14</text>

    <rect x="15" y="340" width="180" height="45" rx="6" fill="#f8fafc" stroke="#e2e8f0" />
    <text x="105" y="367" text-anchor="middle" font-family="Consolas" font-weight="bold" font-size="12" fill="#1e40af">Y = !(A·B)</text>
  </g>

  <!-- 3. 74LS04 -->
  <g transform="translate(505, 85)" filter="url(#shadow)">
    <rect width="210" height="400" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="105" y="30" text-anchor="middle" class="chip-t">74LS04</text>
    <text x="105" y="48" text-anchor="middle" class="gate-txt">六 反相器</text>

    <rect x="55" y="65" width="100" height="260" rx="6" fill="#1e293b" />
    <path d="M 95 65 A 10 10 0 0 0 115 65" fill="#ffffff" />

    <line x1="25" y1="85" x2="55" y2="85" stroke="#64748b" stroke-width="3" /><text x="18" y="89" text-anchor="end" class="pin-name">1A</text><text x="63" y="89" class="pin-num" fill="#fff">1</text>
    <line x1="25" y1="120" x2="55" y2="120" stroke="#2563eb" stroke-width="3" /><text x="18" y="124" text-anchor="end" class="pin-name" fill="#2563eb">1Y</text><text x="63" y="124" class="pin-num" fill="#fff">2</text>
    <line x1="25" y1="155" x2="55" y2="155" stroke="#64748b" stroke-width="3" /><text x="18" y="159" text-anchor="end" class="pin-name">2A</text><text x="63" y="159" class="pin-num" fill="#fff">3</text>
    <line x1="25" y1="190" x2="55" y2="190" stroke="#2563eb" stroke-width="3" /><text x="18" y="194" text-anchor="end" class="pin-name" fill="#2563eb">2Y</text><text x="63" y="194" class="pin-num" fill="#fff">4</text>
    <line x1="25" y1="225" x2="55" y2="225" stroke="#64748b" stroke-width="3" /><text x="18" y="229" text-anchor="end" class="pin-name">3A</text><text x="63" y="229" class="pin-num" fill="#fff">5</text>
    <line x1="25" y1="260" x2="55" y2="260" stroke="#2563eb" stroke-width="3" /><text x="18" y="264" text-anchor="end" class="pin-name" fill="#2563eb">3Y</text><text x="63" y="264" class="pin-num" fill="#fff">6</text>
    <line x1="25" y1="295" x2="55" y2="295" stroke="#0f172a" stroke-width="3" /><text x="18" y="299" text-anchor="end" class="pin-name">GND</text><text x="63" y="299" class="pin-num" fill="#fff">7</text>

    <!-- 右侧: 4Y, 4A, 5Y, 5A, 6Y, 6A, Vcc -->
    <line x1="155" y1="295" x2="185" y2="295" stroke="#2563eb" stroke-width="3" /><text x="192" y="299" class="pin-name" fill="#2563eb">4Y</text><text x="142" y="299" class="pin-num" fill="#fff">8</text>
    <line x1="155" y1="260" x2="185" y2="260" stroke="#64748b" stroke-width="3" /><text x="192" y="264" class="pin-name">4A</text><text x="142" y="264" class="pin-num" fill="#fff">9</text>
    <line x1="155" y1="225" x2="185" y2="225" stroke="#2563eb" stroke-width="3" /><text x="192" y="229" class="pin-name" fill="#2563eb">5Y</text><text x="138" y="229" class="pin-num" fill="#fff">10</text>
    <line x1="155" y1="190" x2="185" y2="190" stroke="#64748b" stroke-width="3" /><text x="192" y="194" class="pin-name">5A</text><text x="138" y="194" class="pin-num" fill="#fff">11</text>
    <line x1="155" y1="155" x2="185" y2="155" stroke="#2563eb" stroke-width="3" /><text x="192" y="159" class="pin-name" fill="#2563eb">6Y</text><text x="138" y="159" class="pin-num" fill="#fff">12</text>
    <line x1="155" y1="120" x2="185" y2="120" stroke="#64748b" stroke-width="3" /><text x="192" y="124" class="pin-name">6A</text><text x="138" y="124" class="pin-num" fill="#fff">13</text>
    <line x1="155" y1="85" x2="185" y2="85" stroke="#dc2626" stroke-width="3" /><text x="192" y="89" class="pin-name" fill="#dc2626">Vcc</text><text x="138" y="89" class="pin-num" fill="#fff">14</text>

    <rect x="15" y="340" width="180" height="45" rx="6" fill="#f8fafc" stroke="#e2e8f0" />
    <text x="105" y="367" text-anchor="middle" font-family="Consolas" font-weight="bold" font-size="12" fill="#1e40af">Y = !A (反相)</text>
  </g>

  <!-- 4. 74LS125 -->
  <g transform="translate(735, 85)" filter="url(#shadow)">
    <rect width="210" height="400" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="105" y="30" text-anchor="middle" class="chip-t">74LS125</text>
    <text x="105" y="48" text-anchor="middle" class="gate-txt">四 三态总线缓冲门</text>

    <rect x="55" y="65" width="100" height="260" rx="6" fill="#1e293b" />
    <path d="M 95 65 A 10 10 0 0 0 115 65" fill="#ffffff" />

    <!-- !1EN, 1A, 1Q, !2EN, 2A, 2Q, GND -->
    <line x1="25" y1="85" x2="55" y2="85" stroke="#d97706" stroke-width="3" /><text x="18" y="89" text-anchor="end" class="pin-name" fill="#d97706">/1EN</text><text x="63" y="89" class="pin-num" fill="#fff">1</text>
    <line x1="25" y1="120" x2="55" y2="120" stroke="#64748b" stroke-width="3" /><text x="18" y="124" text-anchor="end" class="pin-name">1A</text><text x="63" y="124" class="pin-num" fill="#fff">2</text>
    <line x1="25" y1="155" x2="55" y2="155" stroke="#2563eb" stroke-width="3" /><text x="18" y="159" text-anchor="end" class="pin-name" fill="#2563eb">1Q</text><text x="63" y="159" class="pin-num" fill="#fff">3</text>
    <line x1="25" y1="190" x2="55" y2="190" stroke="#d97706" stroke-width="3" /><text x="18" y="194" text-anchor="end" class="pin-name" fill="#d97706">/2EN</text><text x="63" y="194" class="pin-num" fill="#fff">4</text>
    <line x1="25" y1="225" x2="55" y2="225" stroke="#64748b" stroke-width="3" /><text x="18" y="229" text-anchor="end" class="pin-name">2A</text><text x="63" y="229" class="pin-num" fill="#fff">5</text>
    <line x1="25" y1="260" x2="55" y2="260" stroke="#2563eb" stroke-width="3" /><text x="18" y="264" text-anchor="end" class="pin-name" fill="#2563eb">2Q</text><text x="63" y="264" class="pin-num" fill="#fff">6</text>
    <line x1="25" y1="295" x2="55" y2="295" stroke="#0f172a" stroke-width="3" /><text x="18" y="299" text-anchor="end" class="pin-name">GND</text><text x="63" y="299" class="pin-num" fill="#fff">7</text>

    <!-- 右侧: 3Q, 3A, /3EN, 4Q, 4A, /4EN, Vcc -->
    <line x1="155" y1="295" x2="185" y2="295" stroke="#2563eb" stroke-width="3" /><text x="192" y="299" class="pin-name" fill="#2563eb">3Q</text><text x="142" y="299" class="pin-num" fill="#fff">8</text>
    <line x1="155" y1="260" x2="185" y2="260" stroke="#64748b" stroke-width="3" /><text x="192" y="264" class="pin-name">3A</text><text x="142" y="264" class="pin-num" fill="#fff">9</text>
    <line x1="155" y1="225" x2="185" y2="225" stroke="#d97706" stroke-width="3" /><text x="192" y="229" class="pin-name" fill="#d97706">/3EN</text><text x="138" y="229" class="pin-num" fill="#fff">10</text>
    <line x1="155" y1="190" x2="185" y2="190" stroke="#2563eb" stroke-width="3" /><text x="192" y="194" class="pin-name" fill="#2563eb">4Q</text><text x="138" y="194" class="pin-num" fill="#fff">11</text>
    <line x1="155" y1="155" x2="185" y2="155" stroke="#64748b" stroke-width="3" /><text x="192" y="159" class="pin-name">4A</text><text x="138" y="159" class="pin-num" fill="#fff">12</text>
    <line x1="155" y1="120" x2="185" y2="120" stroke="#d97706" stroke-width="3" /><text x="192" y="124" class="pin-name" fill="#d97706">/4EN</text><text x="138" y="124" class="pin-num" fill="#fff">13</text>
    <line x1="155" y1="85" x2="185" y2="85" stroke="#dc2626" stroke-width="3" /><text x="192" y="89" class="pin-name" fill="#dc2626">Vcc</text><text x="138" y="89" class="pin-num" fill="#fff">14</text>

    <rect x="15" y="340" width="180" height="45" rx="6" fill="#f8fafc" stroke="#e2e8f0" />
    <text x="105" y="360" text-anchor="middle" font-size="11" font-weight="bold" fill="#d97706">/EN=0 时 Q = A</text>
    <text x="105" y="378" text-anchor="middle" font-size="11" font-weight="bold" fill="#b91c1c">/EN=1 时 高阻态 Hi-Z</text>
  </g>

  <!-- 底部关键提示 -->
  <rect x="45" y="500" width="900" height="60" rx="8" fill="#eff6ff" stroke="#bfdbfe" />
  <text x="65" y="525" font-family="sans-serif" font-weight="bold" font-size="12" fill="#1e40af">💡 TTL 门电路引脚识别与悬空特性规则：</text>
  <text x="65" y="545" font-family="sans-serif" font-size="11" fill="#1d4ed8">
    正对缺口朝上，左下角为 7 脚 (GND 接地)，右上角为 14 脚 (Vcc 接 +5V)。TTL 与非门输入端悬空相当于逻辑高电平“1”；但不使用的输入端建议接 +5V 或并接有效输入端，禁止悬空以防噪声干扰。
  </text>
</svg>'''

with open("images/exp_dig1_gate_conversion.svg", "w", encoding="utf-8") as f:
    # 2. exp_dig1_gate_conversion.svg: 与非门构成或门、或非门、异或门
    dig1_fig2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 560" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .card-t { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 15px; font-weight: bold; fill: #1e3a8a; }
      .math { font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; fill: #2563eb; }
      .pin { font-family: 'Consolas', monospace; font-size: 11px; font-weight: bold; fill: #0f172a; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="980" height="560" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />

  <text x="490" y="38" text-anchor="middle" class="title">图 1-2 利用与非门 (74LS00) 构成其它常用基本逻辑门电路</text>
  <text x="490" y="60" text-anchor="middle" class="sub">基于摩根定律的与非转换：或门 (图1-3) · 或非门 (图1-4) · 异或门 (图1-5)</text>

  <!-- 3 个逻辑电路卡片，左: 或门, 中: 或非门, 右: 异或门 -->

  <!-- 1. 组成或门 (图 1-3) -->
  <g transform="translate(40, 85)" filter="url(#shadow)">
    <rect width="280" height="380" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="30" class="card-t">1. 组成或门 (OR Gate)</text>
    <text x="20" y="52" class="math">Y = A + B = !(!A · !B)</text>
    <text x="20" y="70" font-size="11" fill="#64748b">需用 3 个 2 输入与非门</text>

    <!-- 逻辑图 -->
    <g transform="translate(25, 95)">
      <!-- 输入 A -->
      <line x1="10" y1="35" x2="45" y2="25" stroke="#0f172a" stroke-width="2" />
      <line x1="10" y1="35" x2="45" y2="45" stroke="#0f172a" stroke-width="2" />
      <circle cx="10" cy="35" r="3" fill="#2563eb" /><text x="5" y="38" text-anchor="end" class="pin">A</text>
      <!-- 与非门 1 (做非门) -->
      <path d="M 45 15 L 65 15 A 20 20 0 0 1 65 55 L 45 55 Z" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
      <circle cx="89" cy="35" r="4" fill="#ffffff" stroke="#2563eb" stroke-width="2" />
      <text x="56" y="39" font-size="13" font-weight="bold" fill="#2563eb">&amp;</text>
      <!-- 输出 !A -->
      <line x1="93" y1="35" x2="140" y2="70" stroke="#0f172a" stroke-width="2" />

      <!-- 输入 B -->
      <line x1="10" y1="125" x2="45" y2="115" stroke="#0f172a" stroke-width="2" />
      <line x1="10" y1="125" x2="45" y2="135" stroke="#0f172a" stroke-width="2" />
      <circle cx="10" cy="125" r="3" fill="#2563eb" /><text x="5" y="128" text-anchor="end" class="pin">B</text>
      <!-- 与非门 2 (做非门) -->
      <path d="M 45 105 L 65 105 A 20 20 0 0 1 65 145 L 45 145 Z" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
      <circle cx="89" cy="125" r="4" fill="#ffffff" stroke="#2563eb" stroke-width="2" />
      <text x="56" y="129" font-size="13" font-weight="bold" fill="#2563eb">&amp;</text>
      <!-- 输出 !B -->
      <line x1="93" y1="125" x2="140" y2="90" stroke="#0f172a" stroke-width="2" />

      <!-- 与非门 3 (总合成) -->
      <path d="M 140 60 L 160 60 A 20 20 0 0 1 160 100 L 140 100 Z" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
      <circle cx="184" cy="80" r="4" fill="#ffffff" stroke="#2563eb" stroke-width="2" />
      <text x="151" y="84" font-size="13" font-weight="bold" fill="#2563eb">&amp;</text>
      
      <!-- 输出 Y 接 LED -->
      <line x1="188" y1="80" x2="225" y2="80" stroke="#0f172a" stroke-width="2" />
      <circle cx="225" cy="80" r="4" fill="#10b981" />
      <text x="235" y="84" class="pin" fill="#10b981">Y</text>
    </g>

    <!-- 真值表 1-2 -->
    <g transform="translate(20, 260)">
      <rect width="240" height="100" rx="6" fill="#f8fafc" stroke="#cbd5e1" />
      <text x="120" y="22" text-anchor="middle" font-weight="bold" font-size="12" fill="#0f172a">表 1-2 或门测试真值表</text>
      <text x="30" y="44" font-family="Consolas" font-size="11">A  B | Y (LED)</text>
      <text x="30" y="62" font-family="Consolas" font-size="11">0  0 | 0 (灭)</text>
      <text x="30" y="80" font-family="Consolas" font-size="11">0  1 | 1 (亮)  1  0 | 1 (亮)</text>
      <text x="30" y="94" font-family="Consolas" font-size="11">1  1 | 1 (亮)</text>
    </g>
  </g>

  <!-- 2. 组成或非门 (图 1-4) -->
  <g transform="translate(340, 85)" filter="url(#shadow)">
    <rect width="280" height="380" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="30" class="card-t">2. 组成或非门 (NOR Gate)</text>
    <text x="20" y="52" class="math">Y = !(A + B) = !A · !B</text>
    <text x="20" y="70" font-size="11" fill="#64748b">在或门输出端再加 1 级反相</text>

    <g transform="translate(15, 95)">
      <!-- 前级或门框架简写 -->
      <rect x="10" y="40" width="130" height="80" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-dasharray="3,2" />
      <text x="75" y="85" text-anchor="middle" font-size="11" font-weight="bold" fill="#2563eb">或门电路 (3门)</text>
      <!-- 输出进入第 4 个与非门 (做非门) -->
      <line x1="140" y1="80" x2="165" y2="70" stroke="#0f172a" stroke-width="2" />
      <line x1="140" y1="80" x2="165" y2="90" stroke="#0f172a" stroke-width="2" />

      <path d="M 165 60 L 185 60 A 20 20 0 0 1 185 100 L 165 100 Z" fill="#fee2e2" stroke="#dc2626" stroke-width="2" />
      <circle cx="209" cy="80" r="4" fill="#ffffff" stroke="#dc2626" stroke-width="2" />
      <text x="176" y="84" font-size="13" font-weight="bold" fill="#dc2626">&amp;</text>

      <line x1="213" y1="80" x2="245" y2="80" stroke="#0f172a" stroke-width="2" />
      <circle cx="245" cy="80" r="4" fill="#10b981" />
      <text x="245" y="70" class="pin" fill="#10b981">Y</text>
    </g>

    <!-- 真值表 1-3 -->
    <g transform="translate(20, 260)">
      <rect width="240" height="100" rx="6" fill="#f8fafc" stroke="#cbd5e1" />
      <text x="120" y="22" text-anchor="middle" font-weight="bold" font-size="12" fill="#0f172a">表 1-3 或非门测试真值表</text>
      <text x="30" y="44" font-family="Consolas" font-size="11">A  B | Y (LED)</text>
      <text x="30" y="62" font-family="Consolas" font-size="11">0  0 | 1 (亮 - 仅此为高)</text>
      <text x="30" y="80" font-family="Consolas" font-size="11">0  1 | 0 (灭)  1  0 | 0 (灭)</text>
      <text x="30" y="94" font-family="Consolas" font-size="11">1  1 | 0 (灭)</text>
    </g>
  </g>

  <!-- 3. 组成异或门 (图 1-5) -->
  <g transform="translate(640, 85)" filter="url(#shadow)">
    <rect width="300" height="380" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="30" class="card-t">3. 组成异或门 (XOR Gate)</text>
    <text x="20" y="52" class="math">Y = A ⊕ B = A·!B + !A·B</text>
    <text x="20" y="70" font-size="11" fill="#64748b">经摩根定律转换，用 4 个与非门构成</text>

    <!-- 异或门逻辑结构 -->
    <g transform="translate(15, 90)">
      <!-- 门 1 (产生 !(AB)) -->
      <line x1="15" y1="40" x2="45" y2="40" stroke="#0f172a" stroke-width="1.8" /><text x="8" y="43" class="pin">A</text>
      <line x1="15" y1="80" x2="45" y2="80" stroke="#0f172a" stroke-width="1.8" /><text x="8" y="83" class="pin">B</text>
      <path d="M 45 30 L 65 30 A 20 20 0 0 1 65 90 L 45 90 Z" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
      <circle cx="89" cy="60" r="4" fill="#ffffff" stroke="#2563eb" stroke-width="2" />
      <text x="56" y="64" font-size="13" font-weight="bold" fill="#2563eb">&amp;</text>
      <text x="96" y="52" font-size="10" fill="#2563eb">!(AB)</text>

      <!-- 门 2 (上): 输入 A 与 !(AB) -->
      <path d="M 130 15 L 150 15 A 18 18 0 0 1 150 55 L 130 55 Z" fill="#eff6ff" stroke="#2563eb" stroke-width="1.8" />
      <circle cx="171" cy="35" r="3" fill="#ffffff" stroke="#2563eb" stroke-width="1.8" />

      <!-- 门 3 (下): 输入 B 与 !(AB) -->
      <path d="M 130 65 L 150 65 A 18 18 0 0 1 150 105 L 130 105 Z" fill="#eff6ff" stroke="#2563eb" stroke-width="1.8" />
      <circle cx="171" cy="85" r="3" fill="#ffffff" stroke="#2563eb" stroke-width="1.8" />

      <!-- 交叉引线 -->
      <line x1="89" y1="60" x2="130" y2="45" stroke="#0f172a" stroke-width="1.5" />
      <line x1="89" y1="60" x2="130" y2="75" stroke="#0f172a" stroke-width="1.5" />

      <!-- 门 4 (输出门) -->
      <line x1="174" y1="35" x2="210" y2="50" stroke="#0f172a" stroke-width="1.5" />
      <line x1="174" y1="85" x2="210" y2="70" stroke="#0f172a" stroke-width="1.5" />
      <path d="M 210 40 L 230 40 A 20 20 0 0 1 230 80 L 210 80 Z" fill="#fef3c7" stroke="#d97706" stroke-width="2" />
      <circle cx="254" cy="60" r="4" fill="#ffffff" stroke="#d97706" stroke-width="2" />
      <line x1="258" y1="60" x2="275" y2="60" stroke="#0f172a" stroke-width="2" />
      <circle cx="275" cy="60" r="4" fill="#10b981" /><text x="280" y="64" class="pin" fill="#10b981">Y</text>
    </g>

    <!-- 真值表 1-4 -->
    <g transform="translate(20, 260)">
      <rect width="260" height="100" rx="6" fill="#f8fafc" stroke="#cbd5e1" />
      <text x="130" y="22" text-anchor="middle" font-weight="bold" font-size="12" fill="#0f172a">表 1-4 异或门测试真值表</text>
      <text x="30" y="44" font-family="Consolas" font-size="11">A  B | Y (LED)  逻辑特征</text>
      <text x="30" y="62" font-family="Consolas" font-size="11">0  0 | 0 (灭)    相同为 0</text>
      <text x="30" y="80" font-family="Consolas" font-size="11">0  1 | 1 (亮)    相异为 1</text>
      <text x="30" y="94" font-family="Consolas" font-size="11">1  0 | 1 (亮)    1  1 | 0 (灭)</text>
    </g>
  </g>

  <!-- 底部关键 -->
  <rect x="40" y="480" width="900" height="60" rx="8" fill="#fef3c7" stroke="#fde68a" />
  <text x="60" y="505" font-family="sans-serif" font-weight="bold" font-size="12" fill="#92400e">⚡ 为什么与非门是“万能门”？（思考题 1 核心）：</text>
  <text x="60" y="525" font-family="sans-serif" font-size="11" fill="#78350f">
    与非逻辑具备完备性，任何复杂的组合逻辑函数均可通过德摩根定律转化为“与非-与非”形式，用单一型号芯片 (74LS00) 即可搭建全部数字逻辑！
  </text>
</svg>'''
    f.write(dig1_fig2)

print("dig1_gate_conversion generated")

with open("images/exp_dig1_gate_pinouts.svg", "w", encoding="utf-8") as f:
    f.write(dig1_fig1)

print("dig1_gate_pinouts generated")

# 3. exp_dig1_ring_oscillator_tristate.svg (反相器多谐振荡器与三态门应用)
dig1_fig3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 540" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .h2 { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 15px; font-weight: bold; fill: #1e3a8a; }
      .math { font-family: 'Consolas', monospace; font-size: 13px; font-weight: bold; }
      .desc { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 11px; fill: #475569; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="980" height="540" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />

  <text x="490" y="38" text-anchor="middle" class="title">图 1-3 反相器多谐振荡器 (图1-6) 与 74LS125 三态门总线应用 (图1-7)</text>
  <text x="490" y="60" text-anchor="middle" class="sub">周期性时钟脉冲产生 · 三态控制 · 数据双向/单向总线传输</text>

  <!-- 左侧：反相器多谐振荡器 (图 1-6) -->
  <g transform="translate(40, 85)" filter="url(#shadow)">
    <rect width="430" height="420" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="30" class="h2">1. 反相器组成的多谐振荡器 (图 1-6)</text>
    
    <!-- 电路绘制 -->
    <g transform="translate(30, 60)">
      <!-- 反相器 G1 -->
      <polygon points="40,30 40,70 75,50" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
      <circle cx="80" cy="50" r="4" fill="#ffffff" stroke="#2563eb" stroke-width="2" />
      <text x="48" y="54" font-size="11" font-weight="bold" fill="#2563eb">G1</text>
      
      <!-- 连线到 G2 -->
      <line x1="84" y1="50" x2="120" y2="50" stroke="#0f172a" stroke-width="2" />
      <polygon points="120,30 120,70 155,50" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
      <circle cx="160" cy="50" r="4" fill="#ffffff" stroke="#2563eb" stroke-width="2" />
      <text x="128" y="54" font-size="11" font-weight="bold" fill="#2563eb">G2</text>

      <!-- 输出 uo -->
      <line x1="164" y1="50" x2="220" y2="50" stroke="#0f172a" stroke-width="2" />
      <circle cx="220" cy="50" r="4" fill="#10b981" />
      <text x="230" y="55" font-size="13" font-weight="bold" fill="#10b981">uo</text>

      <!-- 反馈回路：电容 C 跨接在 G2 输出与输入之间 -->
      <line x1="180" y1="50" x2="180" y2="120" stroke="#0f172a" stroke-width="2" />
      <line x1="180" y1="120" x2="135" y2="120" stroke="#0f172a" stroke-width="2" />
      <!-- 电容 C = 0.01uF -->
      <line x1="135" y1="110" x2="135" y2="130" stroke="#0f172a" stroke-width="2.5" />
      <line x1="127" y1="110" x2="127" y2="130" stroke="#0f172a" stroke-width="2.5" />
      <text x="131" y="145" text-anchor="middle" font-size="10" font-weight="bold">C=0.01μF</text>
      <line x1="127" y1="120" x2="80" y2="120" stroke="#0f172a" stroke-width="2" />
      
      <!-- 电阻 R = 1k 与 Rs = 10k -->
      <!-- 电阻 R -->
      <rect x="50" y="112" width="30" height="16" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.8" />
      <text x="65" y="124" text-anchor="middle" font-size="9" font-weight="bold">R=1k</text>
      <line x1="50" y1="120" x2="20" y2="120" stroke="#0f172a" stroke-width="2" />
      <line x1="20" y1="120" x2="20" y2="50" stroke="#0f172a" stroke-width="2" />
      <!-- 电阻 Rs -->
      <rect x="5" y="65" width="16" height="30" fill="#f1f5f9" stroke="#0f172a" stroke-width="1.8" />
      <text x="32" y="82" font-size="9" font-weight="bold">Rs=10k</text>
      <line x1="20" y1="50" x2="40" y2="50" stroke="#0f172a" stroke-width="2" />
      <!-- 接地中间节点 -->
      <line x1="80" y1="120" x2="102" y2="50" stroke="#0f172a" stroke-width="2" />
    </g>

    <!-- 频率公式与测试数据看板 -->
    <g transform="translate(20, 220)">
      <rect width="390" height="175" rx="8" fill="#f8fafc" stroke="#cbd5e1" />
      <text x="15" y="25" font-size="12" font-weight="bold" fill="#0f172a">📐 频率理论计算与示波器实测对比：</text>
      <text x="15" y="50" class="math" fill="#b91c1c">理论公式：f = 1 / T = 1 / (2.2 · R · C)</text>
      <text x="15" y="72" class="desc">代入 R = 1.0 kΩ, C = 0.01 μF：</text>
      <text x="15" y="92" class="math" fill="#1e40af">f = 1 / (2.2 × 1000 × 10^-8) ≈ 45.45 kHz</text>
      
      <rect x="15" y="105" width="360" height="55" rx="6" fill="#ecfdf5" stroke="#a7f3d0" />
      <text x="25" y="125" font-size="11" font-weight="bold" fill="#065f46">📊 示波器实测波形参数：</text>
      <text x="25" y="145" font-size="10" fill="#047857">实测周期 T = 22.4 µs ➔ 实测频率 f = 44.64 kHz (误差仅 -1.8%)，输出标准矩形波。</text>
    </g>
  </g>

  <!-- 右侧：三态门应用 (图 1-7) -->
  <g transform="translate(500, 85)" filter="url(#shadow)">
    <rect width="440" height="420" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="30" class="h2">2. 74LS125 三态门总线应用 (图 1-7)</text>

    <!-- (a) 多路开关 -->
    <g transform="translate(20, 48)">
      <rect width="400" height="105" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
      <text x="15" y="22" font-size="12" font-weight="bold" fill="#0f172a">图 1-7(a) 多路选择开关（表 1-5）</text>
      <text x="15" y="45" class="desc">由同一控制信号 /EN 反相分别控制两片三态门：</text>
      <text x="15" y="65" font-family="Consolas" font-size="11" fill="#1e40af">当 /EN = 0 时，门1选通 ➔ 输出 L = A1；</text>
      <text x="15" y="85" font-family="Consolas" font-size="11" fill="#1e40af">当 /EN = 1 时，门2选通 ➔ 输出 L = A2。</text>
    </g>

    <!-- (b) 数据双向传输 -->
    <g transform="translate(20, 165)">
      <rect width="400" height="105" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
      <text x="15" y="22" font-size="12" font-weight="bold" fill="#0f172a">图 1-7(b) 数据双向传输（表 1-6）</text>
      <text x="15" y="45" class="desc">两个三态门反向并联跨接在 A1 与 A2 之间：</text>
      <text x="15" y="65" font-family="Consolas" font-size="11" fill="#047857">当 /EN = 0 时，正向门通 ➔ A1 ➔ A2 数据流动；</text>
      <text x="15" y="85" font-family="Consolas" font-size="11" fill="#047857">当 /EN = 1 时，反向门通 ➔ A2 ➔ A1 反向传输。</text>
    </g>

    <!-- (c) 单向总线传输 -->
    <g transform="translate(20, 282)">
      <rect width="400" height="115" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
      <text x="15" y="22" font-size="12" font-weight="bold" fill="#0f172a">图 1-7(c) 单向分时复用总线传输（表 1-7）</text>
      <text x="15" y="45" class="desc">多个信号源输出并联挂在单根数据总线 L 上：</text>
      <text x="15" y="68" font-size="11" fill="#b91c1c">任何时刻只能允许一个三态门的使能端 /EN=0（有效）！</text>
      <text x="15" y="88" font-size="11" fill="#334155">其余三态门必须置于高阻态（Hi-Z），防止总线冲突短路！</text>
    </g>
  </g>
</svg>'''

with open("images/exp_dig1_ring_oscillator_tristate.svg", "w", encoding="utf-8") as f:
    f.write(dig1_fig3)

print("dig1_ring_oscillator_tristate generated")

# 4. exp_dig1_responder_rs_trigger.svg (四人抢答器逻辑电路图与基本RS触发器)
dig1_fig4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 540" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .h2 { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 15px; font-weight: bold; fill: #1e3a8a; }
      .txt { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 11px; fill: #334155; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="980" height="540" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />

  <text x="490" y="38" text-anchor="middle" class="title">图 1-4 四人智力抢答器逻辑电路 (图1-8) 与基本 RS 触发器 (图1-9)</text>
  <text x="490" y="60" text-anchor="middle" class="sub">74LS20 (4输入与非) + 74LS04 (反相器) 自锁鉴优电路 · RS 触发器置位/复位逻辑</text>

  <!-- 左侧：四人抢答器电路原理 (图 1-8) -->
  <g transform="translate(40, 85)" filter="url(#shadow)">
    <rect width="460" height="420" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="30" class="h2">1. 四人抢答逻辑电路原理（思考题 6 详解）</text>

    <!-- 抢答按键 K1~K4 与自锁逻辑 -->
    <g transform="translate(20, 50)">
      <rect width="420" height="230" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
      <text x="15" y="25" font-size="12" font-weight="bold" fill="#0f172a">工作原理机制：</text>
      <text x="15" y="48" class="txt">1. <tspan font-weight="bold">准备状态：</tspan>主持人未宣布开始时，抢答开关断开，四路输入均为 1，指示灯全灭。</text>
      <text x="15" y="75" class="txt">2. <tspan font-weight="bold">率先抢答：</tspan>某选手（如 1 号）率先按下开关 K1 ➔ 该路产生低电平 0 ➔ 驱动对应指示灯 L1 点亮！</text>
      <text x="15" y="112" class="txt">3. <tspan font-weight="bold">全局互锁自锁：</tspan>1 号抢答信号通过 4 输入与非门 (74LS20) 产生封锁反馈信号，瞬间将另外 3 路与非门全部封闭！</text>
      <text x="15" y="150" class="txt">4. <tspan font-weight="bold">鉴优排他性：</tspan>其余选手随后再按下 K2、K3、K4 均完全无效，指示灯不亮，实现严格“第一优先”！</text>
      
      <!-- 逻辑表达式 -->
      <rect x="15" y="175" width="390" height="42" rx="6" fill="#eff6ff" stroke="#bfdbfe" />
      <text x="25" y="200" font-family="Consolas" font-weight="bold" font-size="12" fill="#1e40af">Li = !(Ki · !LOCK), 其中 LOCK = !(K1·K2·K3·K4)</text>
    </g>

    <!-- 底部实测特点 -->
    <rect x="20" y="295" width="420" height="100" rx="8" fill="#ecfdf5" stroke="#a7f3d0" />
    <text x="30" y="320" font-size="12" font-weight="bold" fill="#065f46">🏆 抢答器实验实测结论：</text>
    <text x="30" y="342" font-size="11" fill="#047857">● 任何一人抢按，对应指示灯瞬间点亮，其余3人同时按键毫无反应；</text>
    <text x="30" y="362" font-size="11" fill="#047857">● 松开复位开关后，系统恢复初始待命状态，准确率 100%。</text>
  </g>

  <!-- 右侧：基本 RS 触发器 (图 1-9) -->
  <g transform="translate(530, 85)" filter="url(#shadow)">
    <rect width="410" height="420" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="30" class="h2">2. 与非门构成的基本 RS 触发器 (图 1-9 a)</text>

    <!-- RS 触发器电路 -->
    <g transform="translate(30, 50)">
      <!-- 门 1 (上) -->
      <line x1="20" y1="35" x2="60" y2="35" stroke="#0f172a" stroke-width="2" /><text x="10" y="39" class="pin">!S</text>
      <path d="M 60 20 L 80 20 A 20 20 0 0 1 80 60 L 60 60 Z" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
      <circle cx="104" cy="40" r="4" fill="#ffffff" stroke="#2563eb" stroke-width="2" />
      <text x="71" y="44" font-size="13" font-weight="bold" fill="#2563eb">&amp;</text>
      <line x1="108" y1="40" x2="160" y2="40" stroke="#0f172a" stroke-width="2" /><circle cx="160" cy="40" r="4" fill="#10b981" /><text x="170" y="44" class="pin" fill="#10b981">Q</text>

      <!-- 门 2 (下) -->
      <line x1="20" y1="125" x2="60" y2="125" stroke="#0f172a" stroke-width="2" /><text x="10" y="129" class="pin">!R</text>
      <path d="M 60 105 L 80 105 A 20 20 0 0 1 80 145 L 60 145 Z" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
      <circle cx="104" cy="125" r="4" fill="#ffffff" stroke="#2563eb" stroke-width="2" />
      <text x="71" y="129" font-size="13" font-weight="bold" fill="#2563eb">&amp;</text>
      <line x1="108" y1="125" x2="160" y2="125" stroke="#0f172a" stroke-width="2" /><circle cx="160" cy="125" r="4" fill="#10b981" /><text x="170" y="129" class="pin" fill="#10b981">!Q</text>

      <!-- 交叉互锁反馈线 -->
      <line x1="130" y1="40" x2="130" y2="70" stroke="#dc2626" stroke-width="1.8" />
      <line x1="130" y1="70" x2="45" y2="110" stroke="#dc2626" stroke-width="1.8" />
      <line x1="45" y1="110" x2="60" y2="115" stroke="#dc2626" stroke-width="1.8" />

      <line x1="130" y1="125" x2="130" y2="95" stroke="#2563eb" stroke-width="1.8" />
      <line x1="130" y1="95" x2="45" y2="55" stroke="#2563eb" stroke-width="1.8" />
      <line x1="45" y1="55" x2="60" y2="50" stroke="#2563eb" stroke-width="1.8" />
    </g>

    <!-- 真值表 -->
    <g transform="translate(20, 225)">
      <rect width="370" height="170" rx="8" fill="#f8fafc" stroke="#cbd5e1" />
      <text x="185" y="24" text-anchor="middle" font-weight="bold" font-size="12" fill="#0f172a">基本 RS 触发器功能真值表</text>
      <text x="20" y="50" font-family="Consolas" font-size="11">!S  !R | Q  !Q | 功能说明</text>
      <text x="20" y="75" font-family="Consolas" font-size="11"> 0   1 | 1   0 | 置位 (置 1)</text>
      <text x="20" y="100" font-family="Consolas" font-size="11"> 1   0 | 0   1 | 复位 (清 0)</text>
      <text x="20" y="125" font-family="Consolas" font-size="11"> 1   1 | Q0 !Q0| 保持原有状态 (记忆存储)</text>
      <text x="20" y="150" font-family="Consolas" font-size="11" fill="#dc2626"> 0   0 | 1   1 | 非法状态 (禁止状态)</text>
    </g>
  </g>
</svg>'''

with open("images/exp_dig1_responder_rs_trigger.svg", "w", encoding="utf-8") as f:
    f.write(dig1_fig4)

print("exp_dig1_responder_rs_trigger generated")

# 5. exp_dig2_xor_half_subtractor.svg (74LS86 异或门、半加器、半减器、原码/反码发生器、奇偶校验器)
dig2_fig1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 560" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .h2 { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 14px; font-weight: bold; fill: #1e3a8a; }
      .math { font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; }
      .pin { font-family: 'Consolas', monospace; font-size: 11px; font-weight: bold; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="980" height="560" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />

  <text x="490" y="38" text-anchor="middle" class="title">图 2-1 实验二 异或门 (74LS86) 应用：半加器/半减器 · 原反码 · 奇偶校验</text>
  <text x="490" y="60" text-anchor="middle" class="sub">74LS86 逻辑特性 · 半减器 (图2-3) · 原码/反码发生器 (图2-6) · 四位奇偶校验器 (图2-7)</text>

  <!-- 3 个典型应用模块 -->

  <!-- 1. 半减器 (图 2-3 & 表 2-1) -->
  <g transform="translate(40, 85)" filter="url(#shadow)">
    <rect width="280" height="440" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="28" class="h2">1. 异或门组成半减器 (图 2-3)</text>
    <text x="20" y="50" class="math" fill="#b91c1c">差 D = A ⊕ B</text>
    <text x="20" y="68" class="math" fill="#2563eb">借位 Ci = !A · B</text>

    <!-- 半减器逻辑图 -->
    <g transform="translate(20, 80)">
      <line x1="20" y1="35" x2="60" y2="35" stroke="#0f172a" stroke-width="2" /><text x="10" y="39" class="pin">A</text>
      <line x1="20" y1="75" x2="60" y2="75" stroke="#0f172a" stroke-width="2" /><text x="10" y="79" class="pin">B</text>

      <!-- 异或门 (产生差 D) -->
      <path d="M 60 20 Q 75 45, 60 70 M 65 20 L 75 20 Q 95 45, 75 70 L 65 70 Q 80 45, 65 20" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
      <text x="80" y="49" font-size="12" font-weight="bold" fill="#2563eb">=1</text>
      <line x1="90" y1="45" x2="140" y2="45" stroke="#0f172a" stroke-width="2" />
      <circle cx="140" cy="45" r="4" fill="#10b981" /><text x="150" y="49" class="pin" fill="#10b981">D (差)</text>

      <!-- 与门 + 反相器 (产生借位 Ci) -->
      <line x1="30" y1="35" x2="30" y2="120" stroke="#0f172a" stroke-width="2" />
      <!-- 反相器 !A -->
      <polygon points="30,110 30,130 45,120" fill="#ffffff" stroke="#dc2626" stroke-width="1.8" />
      <circle cx="48" cy="120" r="2.5" fill="#ffffff" stroke="#dc2626" stroke-width="1.8" />
      <line x1="51" y1="120" x2="80" y2="120" stroke="#0f172a" stroke-width="2" />

      <line x1="45" y1="75" x2="45" y2="140" stroke="#0f172a" stroke-width="2" />
      <line x1="45" y1="140" x2="80" y2="140" stroke="#0f172a" stroke-width="2" />

      <!-- 与门 -->
      <path d="M 80 110 L 100 110 A 18 18 0 0 1 100 150 L 80 150 Z" fill="#fee2e2" stroke="#dc2626" stroke-width="2" />
      <text x="90" y="134" font-size="12" font-weight="bold" fill="#dc2626">&amp;</text>
      <line x1="118" y1="130" x2="140" y2="130" stroke="#0f172a" stroke-width="2" />
      <circle cx="140" cy="130" r="4" fill="#ef4444" /><text x="150" y="134" class="pin" fill="#ef4444">Ci (借位)</text>
    </g>

    <!-- 真值表 2-1 -->
    <g transform="translate(15, 260)">
      <rect width="250" height="155" rx="6" fill="#f8fafc" stroke="#cbd5e1" />
      <text x="125" y="24" text-anchor="middle" font-weight="bold" font-size="12" fill="#0f172a">表 2-1 半减器实测真值表</text>
      <text x="25" y="52" font-family="Consolas" font-size="11">A  B | D  Ci | 算术意义</text>
      <text x="25" y="76" font-family="Consolas" font-size="11">0  0 | 0   0 | 0 - 0 = 0</text>
      <text x="25" y="100" font-family="Consolas" font-size="11" fill="#dc2626">0  1 | 1   1 | 0 - 1 = 1 (借1)</text>
      <text x="25" y="124" font-family="Consolas" font-size="11">1  0 | 1   0 | 1 - 0 = 1</text>
      <text x="25" y="146" font-family="Consolas" font-size="11">1  1 | 0   0 | 1 - 1 = 0</text>
    </g>
  </g>

  <!-- 2. 原码/反码发生器 (图 2-6 & 表 2-2) -->
  <g transform="translate(340, 85)" filter="url(#shadow)">
    <rect width="280" height="440" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="28" class="h2">2. 原码/反码发生器 (图 2-6)</text>
    <text x="20" y="50" class="math" fill="#b91c1c">输出 Yi = Di ⊕ M</text>
    <text x="20" y="68" font-size="11" fill="#64748b">M 为控制端 (M=0原码, M=1反码)</text>

    <!-- 4 个异或门阵列示意 -->
    <g transform="translate(20, 85)">
      <rect width="240" height="150" rx="8" fill="#eff6ff" stroke="#bfdbfe" />
      <text x="120" y="25" text-anchor="middle" font-weight="bold" font-size="11" fill="#1e40af">4 位可控原/反码电路</text>
      <text x="20" y="55" font-family="Consolas" font-size="11">控制端 M = 0 时：</text>
      <text x="35" y="75" font-family="Consolas" font-size="11" fill="#047857">Yi = Di ⊕ 0 = Di (原码输出)</text>
      <text x="20" y="105" font-family="Consolas" font-size="11">控制端 M = 1 时：</text>
      <text x="35" y="125" font-family="Consolas" font-size="11" fill="#dc2626">Yi = Di ⊕ 1 = !Di (反码输出)</text>
    </g>

    <!-- 测试数据表 2-2 摘要 -->
    <g transform="translate(15, 260)">
      <rect width="250" height="155" rx="6" fill="#f8fafc" stroke="#cbd5e1" />
      <text x="125" y="24" text-anchor="middle" font-weight="bold" font-size="12" fill="#0f172a">表 2-2 原/反码测试实测</text>
      <text x="20" y="50" font-family="Consolas" font-size="10">M | D4 D3 D2 D1 | Y4 Y3 Y2 Y1</text>
      <text x="20" y="72" font-family="Consolas" font-size="10" fill="#047857">0 | 0  1  0  1  | 0  1  0  1 (原码)</text>
      <text x="20" y="94" font-family="Consolas" font-size="10" fill="#047857">0 | 1  1  0  0  | 1  1  0  0 (原码)</text>
      <text x="20" y="118" font-family="Consolas" font-size="10" fill="#dc2626">1 | 0  1  0  1  | 1  0  1  0 (反码)</text>
      <text x="20" y="140" font-family="Consolas" font-size="10" fill="#dc2626">1 | 1  1  0  0  | 0  0  1  1 (反码)</text>
    </g>
  </g>

  <!-- 3. 奇偶校验器 (图 2-7 & 表 2-3) -->
  <g transform="translate(640, 85)" filter="url(#shadow)">
    <rect width="300" height="440" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="28" class="h2">3. 四位奇偶校验器 (图 2-7)</text>
    <text x="20" y="50" class="math" fill="#b91c1c">Y = A ⊕ B ⊕ C ⊕ D</text>
    <text x="20" y="68" font-size="11" fill="#64748b">1 的个数为奇数时输出 1 (灯亮)</text>

    <!-- 级联异或结构 -->
    <g transform="translate(20, 85)">
      <rect width="260" height="150" rx="8" fill="#fef3c7" stroke="#fde68a" />
      <text x="130" y="25" text-anchor="middle" font-weight="bold" font-size="11" fill="#92400e">级联异或逻辑：</text>
      <text x="20" y="55" font-family="Consolas" font-size="11">Y1 = A ⊕ B</text>
      <text x="20" y="80" font-family="Consolas" font-size="11">Y2 = Y1 ⊕ C = A ⊕ B ⊕ C</text>
      <text x="20" y="105" font-family="Consolas" font-size="11">Y  = Y2 ⊕ D = A ⊕ B ⊕ C ⊕ D</text>
      <text x="20" y="132" font-size="11" font-weight="bold" fill="#b45309">👉 奇数个 1 ➔ 输出高电平 1</text>
    </g>

    <!-- 表 2-3 实测摘要 -->
    <g transform="translate(15, 260)">
      <rect width="270" height="155" rx="6" fill="#f8fafc" stroke="#cbd5e1" />
      <text x="135" y="24" text-anchor="middle" font-weight="bold" font-size="12" fill="#0f172a">表 2-3 奇偶校验实测规律</text>
      <text x="20" y="50" font-family="Consolas" font-size="10">ABCD 代码 | 1的个数 | 指示灯状态</text>
      <text x="20" y="74" font-family="Consolas" font-size="10">1000      | 1 (奇数) | 亮 (逻辑 1)</text>
      <text x="20" y="96" font-family="Consolas" font-size="10">0110      | 2 (偶数) | 灭 (逻辑 0)</text>
      <text x="20" y="118" font-family="Consolas" font-size="10">1101      | 3 (奇数) | 亮 (逻辑 1)</text>
      <text x="20" y="140" font-family="Consolas" font-size="10">1111      | 4 (偶数) | 灭 (逻辑 0)</text>
    </g>
  </g>
</svg>'''

with open("images/exp_dig2_xor_half_subtractor.svg", "w", encoding="utf-8") as f:
    f.write(dig2_fig1)

print("exp_dig2_xor_half_subtractor generated")

# 6. exp_dig2_adder_subtractor_8421.svg (74LS83/283 四位加法器/减法器及 8421 码转余3码电路)
dig2_fig2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 560" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .h2 { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 15px; font-weight: bold; fill: #1e3a8a; }
      .math { font-family: 'Consolas', monospace; font-size: 12px; font-weight: bold; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="980" height="560" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />

  <text x="490" y="38" text-anchor="middle" class="title">图 2-2 74LS83 四位二进制加法/减法器 (图2-8) 与 8421转余3码电路 (图2-9)</text>
  <text x="490" y="60" text-anchor="middle" class="sub">补码减法原理 · M 控制端取反加 1 · 思考题 1 为什么 C0 接地/接高电平深度解析</text>

  <!-- 左侧：四位二进制加法/减法器 (图 2-8) -->
  <g transform="translate(40, 85)" filter="url(#shadow)">
    <rect width="460" height="440" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="28" class="h2">1. 四位加/减法器原理与电路 (图 2-8)</text>

    <!-- 加减法器逻辑模块 -->
    <g transform="translate(25, 45)">
      <!-- 74LS83 芯片框 -->
      <rect x="110" y="30" width="180" height="150" rx="8" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
      <text x="200" y="60" text-anchor="middle" font-family="sans-serif" font-weight="bold" font-size="14" fill="#1e40af">74LS83 (4位全加器)</text>
      
      <!-- 被加数 A -->
      <line x1="20" y1="65" x2="110" y2="65" stroke="#0f172a" stroke-width="2" />
      <text x="15" y="70" text-anchor="end" font-family="Consolas" font-weight="bold">A4..A1</text>
      
      <!-- 加数 B 通过 4 个异或门 -->
      <rect x="25" y="105" width="60" height="40" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.8" />
      <text x="55" y="129" text-anchor="middle" font-size="11" font-weight="bold" fill="#d97706">4×异或门</text>
      <line x1="10" y1="125" x2="25" y2="125" stroke="#0f172a" stroke-width="2" /><text x="5" y="129" text-anchor="end" font-family="Consolas" font-weight="bold">B4..B1</text>
      <line x1="85" y1="125" x2="110" y2="125" stroke="#0f172a" stroke-width="2" />

      <!-- 控制端 M -->
      <line x1="55" y1="165" x2="55" y2="145" stroke="#dc2626" stroke-width="2" />
      <line x1="55" y1="165" x2="150" y2="165" stroke="#dc2626" stroke-width="2" />
      <line x1="150" y1="165" x2="150" y2="180" stroke="#dc2626" stroke-width="2" />
      <circle cx="55" cy="165" r="4" fill="#dc2626" />
      <text x="50" y="185" font-family="Consolas" font-weight="bold" font-size="13" fill="#dc2626">控制端 M</text>
      <text x="150" y="200" text-anchor="middle" font-family="Consolas" font-size="11" font-weight="bold" fill="#dc2626">接 C0 端</text>

      <!-- 输出端 S 和 C4 -->
      <line x1="290" y1="85" x2="380" y2="85" stroke="#0f172a" stroke-width="2" />
      <text x="390" y="90" font-family="Consolas" font-weight="bold" fill="#10b981">F4..F1 (和/差)</text>

      <line x1="290" y1="140" x2="380" y2="140" stroke="#0f172a" stroke-width="2" />
      <text x="390" y="145" font-family="Consolas" font-weight="bold" fill="#2563eb">C4 (进位/借位)</text>
    </g>

    <!-- 工作机制详细解析 (思考题 1 题解) -->
    <g transform="translate(20, 260)">
      <rect width="420" height="160" rx="8" fill="#f8fafc" stroke="#cbd5e1" />
      <text x="15" y="24" font-size="12" font-weight="bold" fill="#0f172a">💡 思考题 1 深度推导：M 控制加减法的补码机理</text>
      
      <text x="15" y="48" font-size="11" font-weight="bold" fill="#047857">● M = 0 时（做加法 A + B）：</text>
      <text x="25" y="66" class="desc">异或门输出原码 Bi ⊕ 0 = Bi；同时 C0 = 0。全加器执行：F = A + B + 0 = A + B。</text>

      <text x="15" y="94" font-size="11" font-weight="bold" fill="#b91c1c">● M = 1 时（做减法 A - B）：</text>
      <text x="25" y="112" class="desc">异或门对加数各位逐位求反 Bi ⊕ 1 = !Bi；同时 C0 = 1！</text>
      <text x="25" y="130" class="desc">在二进制补码运算中：[-B]补 = !B + 1。因此全加器执行：F = A + !B + 1 = A - B！</text>
      <text x="25" y="148" font-size="11" font-weight="bold" fill="#dc2626">这就是做减法时 C0 必须接高电平 1 的本质原因！</text>
    </g>
  </g>

  <!-- 右侧：8421码转换余3码电路 (图 2-9) -->
  <g transform="translate(530, 85)" filter="url(#shadow)">
    <rect width="410" height="440" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="28" class="h2">2. 8421 码转余 3 码电路 (图 2-9)</text>

    <!-- 电路框图 -->
    <g transform="translate(25, 45)">
      <rect x="80" y="30" width="180" height="150" rx="8" fill="#fef2f2" stroke="#ef4444" stroke-width="2" />
      <text x="170" y="60" text-anchor="middle" font-weight="bold" font-size="14" fill="#991b1b">74LS83 全加器</text>

      <!-- 输入 8421 码 A4..A1 -->
      <line x1="10" y1="75" x2="80" y2="75" stroke="#0f172a" stroke-width="2" />
      <text x="5" y="80" text-anchor="end" font-family="Consolas" font-weight="bold">8421码 A4..A1</text>

      <!-- 加数 B 固定接十进制 3 (0011) -->
      <line x1="10" y1="135" x2="80" y2="135" stroke="#dc2626" stroke-width="2" />
      <text x="5" y="132" text-anchor="end" font-family="Consolas" font-weight="bold" fill="#dc2626">固定数 0011</text>
      <text x="5" y="148" text-anchor="end" font-size="10" fill="#64748b">(B4=0,B3=0,B2=1,B1=1)</text>

      <!-- C0 接地 -->
      <line x1="170" y1="180" x2="170" y2="200" stroke="#0f172a" stroke-width="2" />
      <text x="170" y="215" text-anchor="middle" font-size="10" font-weight="bold">C0 = 0 (GND)</text>

      <!-- 输出 余 3 码 -->
      <line x1="260" y1="105" x2="330" y2="105" stroke="#0f172a" stroke-width="2" />
      <text x="340" y="110" font-family="Consolas" font-weight="bold" fill="#10b981">余3码 S4..S1</text>
    </g>

    <!-- 转换真值表 2-6 摘录 -->
    <g transform="translate(20, 260)">
      <rect width="370" height="160" rx="8" fill="#f8fafc" stroke="#cbd5e1" />
      <text x="185" y="24" text-anchor="middle" font-weight="bold" font-size="12" fill="#0f172a">表 2-6 代码转换实测数据对照</text>
      <text x="25" y="50" font-family="Consolas" font-size="11">十进制 | 8421 码 A  | 余 3 码 (A+3)</text>
      <text x="25" y="72" font-family="Consolas" font-size="11">  0    | 0 0 0 0    | 0 0 1 1  (3)</text>
      <text x="25" y="94" font-family="Consolas" font-size="11">  1    | 0 0 0 1    | 0 1 0 0  (4)</text>
      <text x="25" y="116" font-family="Consolas" font-size="11">  5    | 0 1 0 1    | 1 0 0 0  (8)</text>
      <text x="25" y="138" font-family="Consolas" font-size="11">  9    | 1 0 0 1    | 1 1 0 0  (12)</text>
    </g>
  </g>
</svg>'''

with open("images/exp_dig2_adder_subtractor_8421.svg", "w", encoding="utf-8") as f:
    f.write(dig2_fig2)

print("exp_dig2_adder_subtractor_8421 generated")
print("All Digital Circuit SVGs generated!")
