# -*- coding: utf-8 -*-
import os

os.makedirs("images", exist_ok=True)

# 4. Zener Diode Test Circuit & V-I Curve SVG
fig4_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 520" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .panel-h { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 15px; font-weight: bold; fill: #1e293b; }
      .label { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #334155; }
      .math { font-family: 'Consolas', monospace; font-size: 14px; font-weight: bold; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="960" height="520" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />
  
  <text x="480" y="38" text-anchor="middle" class="title">图 1-4 稳压二极管 (2CW53) 性能测试原理、电路图与伏安特性</text>
  <text x="480" y="60" text-anchor="middle" class="sub">测试反向击穿区的稳压特性，验证 Ucc 变化时端电压 Uo 保持恒定的物理机理</text>

  <!-- 左侧：测试原理电路 -->
  <g transform="translate(40, 85)" filter="url(#shadow)">
    <rect width="430" height="340" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="30" class="panel-h">图 1-2(a) 稳压管测试实验接线电路</text>
    
    <!-- 电源符号 Ucc -->
    <circle cx="70" cy="150" r="22" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
    <text x="70" y="145" text-anchor="middle" font-weight="bold" fill="#2563eb" font-size="16">+</text>
    <text x="70" y="165" text-anchor="middle" font-weight="bold" fill="#2563eb" font-size="16">-</text>
    <text x="70" y="195" text-anchor="middle" font-weight="bold" fill="#1e293b" font-size="13">Ucc (9~15V)</text>

    <!-- 导线与限流电阻 R=1k -->
    <path d="M 70 128 L 70 90 L 150 90" fill="none" stroke="#0f172a" stroke-width="2.5" />
    <!-- 限流电阻 矩形 -->
    <rect x="150" y="80" width="65" height="20" fill="#f1f5f9" stroke="#0f172a" stroke-width="2" />
    <text x="182" y="94" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">R = 1kΩ</text>
    <text x="182" y="70" text-anchor="middle" font-size="12" fill="#64748b">限流电阻</text>

    <!-- 导线到节点 -->
    <path d="M 215 90 L 290 90" fill="none" stroke="#0f172a" stroke-width="2.5" />
    <circle cx="290" cy="90" r="4" fill="#0f172a" />
    <!-- 电流方向箭头 -->
    <path d="M 240 85 L 260 85 L 255 80 M 260 85 L 255 90" fill="none" stroke="#dc2626" stroke-width="2" />
    <text x="250" y="75" text-anchor="middle" font-size="12" font-weight="bold" fill="#dc2626">电流 I</text>

    <!-- 稳压二极管 (反向连接：阴极向上接高电位，阳极向下接地) -->
    <path d="M 290 90 L 290 135" fill="none" stroke="#0f172a" stroke-width="2.5" />
    <!-- 稳压管符号 (三角形+弯折阴极线) -->
    <polygon points="275,170 305,170 290,145" fill="#f87171" stroke="#0f172a" stroke-width="2" />
    <!-- 阴极折线 -->
    <path d="M 270 145 L 275 145 L 305 145 L 310 140" fill="none" stroke="#0f172a" stroke-width="2.5" />
    <path d="M 290 170 L 290 220" fill="none" stroke="#0f172a" stroke-width="2.5" />
    <text x="325" y="160" font-weight="bold" font-size="13" fill="#dc2626">2CW53</text>
    <text x="325" y="176" font-size="11" fill="#64748b">(稳压管)</text>

    <!-- 输出测量端 Uo -->
    <path d="M 290 90 L 380 90" fill="none" stroke="#2563eb" stroke-width="2.5" />
    <circle cx="380" cy="90" r="4" fill="#2563eb" />
    <path d="M 290 220 L 380 220" fill="none" stroke="#2563eb" stroke-width="2.5" />
    <circle cx="380" cy="220" r="4" fill="#2563eb" />
    <!-- 电压表 / 测量表 -->
    <circle cx="380" cy="155" r="20" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
    <text x="380" y="161" text-anchor="middle" font-weight="bold" font-size="15" fill="#2563eb">V</text>
    <line x1="380" y1="90" x2="380" y2="135" stroke="#2563eb" stroke-width="2" stroke-dasharray="3,2" />
    <line x1="380" y1="175" x2="380" y2="220" stroke="#2563eb" stroke-width="2" stroke-dasharray="3,2" />
    <text x="415" y="160" font-weight="bold" font-size="14" fill="#1d4ed8">Uo</text>

    <!-- 回路底线与接地 -->
    <path d="M 70 172 L 70 220 L 290 220" fill="none" stroke="#0f172a" stroke-width="2.5" />
    <circle cx="290" cy="220" r="4" fill="#0f172a" />
    <path d="M 290 220 L 290 240 M 280 240 L 300 240 M 283 245 L 297 245 M 287 250 L 293 250" stroke="#0f172a" stroke-width="2" />

    <!-- 公式推导框 -->
    <rect x="20" y="260" width="390" height="65" rx="6" fill="#f8fafc" stroke="#e2e8f0" />
    <text x="30" y="283" class="math" fill="#b91c1c">回路电流计算公式：I = (Ucc - Uo) / R</text>
    <text x="30" y="308" font-size="12" fill="#475569" font-family="sans-serif">
      例：当 Ucc=12V，实测 Uo=7.0V 时，I = (12 - 7.0) / 1k = 5.0 mA。
    </text>
  </g>

  <!-- 右侧：伏安特性曲线与数据规律 -->
  <g transform="translate(490, 85)" filter="url(#shadow)">
    <rect width="430" height="340" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" />
    <text x="20" y="30" class="panel-h">稳压管反向击穿特性与稳压机理</text>

    <!-- 坐标轴 -->
    <g stroke="#334155" stroke-width="2">
      <!-- 横轴 U -->
      <line x1="40" y1="160" x2="390" y2="160" />
      <polygon points="390,157 398,160 390,163" fill="#334155" />
      <text x="390" y="180" font-family="sans-serif" font-weight="bold" font-size="12" fill="#334155">U</text>
      <!-- 纵轴 I -->
      <line x1="260" y1="280" x2="260" y2="50" />
      <polygon points="257,50 260,42 263,50" fill="#334155" />
      <text x="270" y="55" font-family="sans-serif" font-weight="bold" font-size="12" fill="#334155">I</text>
    </g>

    <!-- 原点 -->
    <text x="245" y="175" font-size="11" fill="#64748b">O</text>

    <!-- 正向导通曲线 (第一象限) -->
    <path d="M 260 160 Q 280 160, 285 150 Q 295 100, 310 60" fill="none" stroke="#3b82f6" stroke-width="2.5" />
    <text x="320" y="80" font-size="11" fill="#2563eb">正向导通 (~0.7V)</text>

    <!-- 反向击穿曲线 (第三象限：稳压工作区！) -->
    <path d="M 260 160 L 130 162 Q 115 165, 110 185 L 105 270" fill="none" stroke="#dc2626" stroke-width="3" />
    <!-- 击穿拐点标注 Uz -->
    <circle cx="110" cy="185" r="4" fill="#dc2626" />
    <line x1="110" y1="160" x2="110" y2="185" stroke="#dc2626" stroke-dasharray="2,2" />
    <text x="90" y="152" font-size="12" font-weight="bold" fill="#dc2626">-Uz</text>
    
    <!-- 稳压工作区底色带 -->
    <rect x="95" y="195" width="30" height="70" fill="#fee2e2" opacity="0.6" rx="4" />
    <text x="135" y="235" font-size="12" font-weight="bold" fill="#b91c1c">反向击穿稳压区</text>
    <text x="135" y="252" font-size="11" fill="#64748b">ΔU 极小，但电流 I 急剧变化</text>

    <!-- 底部实测总结 -->
    <rect x="20" y="275" width="390" height="50" rx="6" fill="#f8fafc" stroke="#e2e8f0" />
    <text x="30" y="295" font-size="12" font-weight="bold" fill="#0f172a">📊 表 1-1 实测规律：</text>
    <text x="30" y="313" font-size="11" fill="#475569" font-family="sans-serif">
      Ucc 从 9V ➔ 15V 大幅升高时，Uo 稳定在约 7V，增加的压降均由限流电阻承受。
    </text>
  </g>

  <!-- 底部思考题提示 -->
  <rect x="40" y="440" width="880" height="60" rx="8" fill="#fef3c7" stroke="#fde68a" stroke-width="1.5" />
  <text x="55" y="465" font-family="sans-serif" font-weight="bold" font-size="13" fill="#92400e">⚡ 限流电阻 R 的计算条件（思考题 3 答题要点）：</text>
  <text x="55" y="485" font-family="sans-serif" font-size="12" fill="#78350f">
    必须满足 (UImax - Uz)/(Izmax + ILmin) ≤ R ≤ (UImin - Uz)/(Izmin + ILmax)。既保证在电网低谷时不低于最小稳定电流，又保证在电网高峰负载开路时不烧坏稳压管。
  </text>
</svg>'''

with open("images/fig4_zener_diode_test.svg", "w", encoding="utf-8") as f:
    f.write(fig4_content)

print("fig4 generated")

# 5. LED Test Circuit SVG
fig5_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 480" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .panel-h { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 15px; font-weight: bold; fill: #1e293b; }
      .param { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #334155; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="960" height="480" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />
  
  <text x="480" y="38" text-anchor="middle" class="title">图 1-5 发光二极管 (LED) 测试原理电路与亮度-电流响应关系</text>
  <text x="480" y="60" text-anchor="middle" class="sub">正向导通工作状态、管压降测定、工作电流与发光强度关系分析</text>

  <!-- 左侧：测试电路 -->
  <g transform="translate(40, 85)" filter="url(#shadow)">
    <rect width="430" height="300" rx="12" fill="#ffffff" stroke="#93c5fd" stroke-width="2" />
    <text x="20" y="30" class="panel-h">图 1-2(b) 发光二极管测试接线图</text>
    
    <!-- 电源 Ucc -->
    <circle cx="70" cy="140" r="22" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
    <text x="70" y="135" text-anchor="middle" font-weight="bold" fill="#2563eb" font-size="16">+</text>
    <text x="70" y="155" text-anchor="middle" font-weight="bold" fill="#2563eb" font-size="16">-</text>
    <text x="70" y="185" text-anchor="middle" font-weight="bold" fill="#1e293b" font-size="13">Ucc (3~5V)</text>

    <!-- 导线与限流电阻 R=300 -->
    <path d="M 70 118 L 70 85 L 150 85" fill="none" stroke="#0f172a" stroke-width="2.5" />
    <rect x="150" y="75" width="65" height="20" fill="#f1f5f9" stroke="#0f172a" stroke-width="2" />
    <text x="182" y="89" text-anchor="middle" font-size="11" font-weight="bold" fill="#0f172a">R = 300Ω</text>
    <text x="182" y="65" text-anchor="middle" font-size="12" fill="#64748b">限流保护</text>

    <!-- 到发光管 -->
    <path d="M 215 85 L 290 85 L 290 120" fill="none" stroke="#0f172a" stroke-width="2.5" />
    
    <!-- 发光二极管符号 (正向接入：阳极向上，阴极向下接地) -->
    <polygon points="275,120 305,120 290,145" fill="#22c55e" stroke="#0f172a" stroke-width="2" />
    <line x1="275" y1="145" x2="305" y2="145" stroke="#0f172a" stroke-width="2.5" />
    <path d="M 290 145 L 290 200" fill="none" stroke="#0f172a" stroke-width="2.5" />
    <!-- 发光光线箭头 -->
    <path d="M 305 130 L 325 115 M 325 115 L 320 116 M 325 115 L 324 121" stroke="#16a34a" stroke-width="2" />
    <path d="M 310 140 L 330 125 M 330 125 L 325 126 M 330 125 L 329 131" stroke="#16a34a" stroke-width="2" />
    <text x="335" y="145" font-weight="bold" font-size="13" fill="#15803d">LED (红/绿)</text>

    <!-- 输出电压表 Uo -->
    <path d="M 290 85 L 370 85" fill="none" stroke="#2563eb" stroke-width="2" />
    <circle cx="370" cy="85" r="4" fill="#2563eb" />
    <path d="M 290 200 L 370 200" fill="none" stroke="#2563eb" stroke-width="2" />
    <circle cx="370" cy="200" r="4" fill="#2563eb" />
    <circle cx="370" cy="142" r="18" fill="#eff6ff" stroke="#2563eb" stroke-width="2" />
    <text x="370" y="147" text-anchor="middle" font-weight="bold" font-size="14" fill="#2563eb">V</text>
    <line x1="370" y1="85" x2="370" y2="124" stroke="#2563eb" stroke-width="2" stroke-dasharray="3,2" />
    <line x1="370" y1="160" x2="370" y2="200" stroke="#2563eb" stroke-width="2" stroke-dasharray="3,2" />
    <text x="400" y="147" font-weight="bold" font-size="13" fill="#1d4ed8">Uo</text>

    <!-- 回路与接地 -->
    <path d="M 70 162 L 70 200 L 290 200" fill="none" stroke="#0f172a" stroke-width="2.5" />
    <path d="M 290 200 L 290 220 M 280 220 L 300 220 M 283 225 L 297 225 M 287 230 L 293 230" stroke="#0f172a" stroke-width="2" />

    <!-- 计算公式 -->
    <rect x="20" y="240" width="390" height="45" rx="6" fill="#f8fafc" stroke="#e2e8f0" />
    <text x="30" y="268" font-family="Consolas" font-weight="bold" font-size="13" fill="#b91c1c">工作电流计算：I = (Ucc - Uo) / 300Ω</text>
  </g>

  <!-- 右侧：数据与实测效果对照 -->
  <g transform="translate(490, 85)" filter="url(#shadow)">
    <rect width="430" height="300" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" />
    <text x="20" y="30" class="panel-h">表 1-2 发光二极管实测数据与状态对照</text>

    <!-- 对照卡片 3V -->
    <g transform="translate(20, 50)">
      <rect width="390" height="60" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
      <circle cx="35" cy="30" r="16" fill="#fecaca" />
      <circle cx="35" cy="30" r="8" fill="#ef4444" opacity="0.6" />
      <text x="70" y="25" font-family="sans-serif" font-weight="bold" font-size="13" fill="#1e293b">Ucc = 3V ➔ Uo ≈ 1.85V | I ≈ 3.8 mA</text>
      <text x="70" y="45" font-family="sans-serif" font-size="12" fill="#64748b">发光状态：微亮（电流刚过开启门限阀值）</text>
    </g>

    <!-- 对照卡片 4V -->
    <g transform="translate(20, 125)">
      <rect width="390" height="60" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
      <circle cx="35" cy="30" r="16" fill="#f87171" />
      <circle cx="35" cy="30" r="10" fill="#dc2626" opacity="0.8" />
      <text x="70" y="25" font-family="sans-serif" font-weight="bold" font-size="13" fill="#1e293b">Ucc = 4V ➔ Uo ≈ 1.95V | I ≈ 6.8 mA</text>
      <text x="70" y="45" font-family="sans-serif" font-size="12" fill="#64748b">发光状态：正常明亮（正常工作指示状态）</text>
    </g>

    <!-- 对照卡片 5V -->
    <g transform="translate(20, 200)">
      <rect width="390" height="60" rx="8" fill="#fef2f2" stroke="#fca5a5" />
      <circle cx="35" cy="30" r="18" fill="#ef4444" filter="drop-shadow(0 0 6px #ef4444)" />
      <circle cx="35" cy="30" r="12" fill="#ffffff" opacity="0.6" />
      <text x="70" y="25" font-family="sans-serif" font-weight="bold" font-size="13" fill="#991b1b">Ucc = 5V ➔ Uo ≈ 2.05V | I ≈ 9.8 mA</text>
      <text x="70" y="45" font-family="sans-serif" font-size="12" fill="#b91c1c">发光状态：高度明亮（高驱动状态，不可过载）</text>
    </g>

    <text x="20" y="282" font-size="11" fill="#64748b" font-family="sans-serif">
      💡 结论：LED具有单向导电性；管压降基本恒定（约1.8~2.1V）；电流越大，亮度越高。
    </text>
  </g>

  <!-- 底部强调 -->
  <rect x="40" y="400" width="880" height="55" rx="8" fill="#eff6ff" stroke="#bfdbfe" stroke-width="1.5" />
  <text x="55" y="425" font-family="sans-serif" font-weight="bold" font-size="13" fill="#1e40af">⚠️ 保护警告：</text>
  <text x="55" y="443" font-family="sans-serif" font-size="12" fill="#1d4ed8">
    严禁将 LED 或稳压管直接跨接在稳压电源两端！必须串联限流电阻 R，否则管子将因无受限大电流瞬间烧毁。
  </text>
</svg>'''

with open("images/fig5_led_test.svg", "w", encoding="utf-8") as f:
    f.write(fig5_content)

print("fig5 generated")

# 6. Multimeter Pinout Check SVG
fig6_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 600" width="100%" height="100%">
  <defs>
    <style>
      .title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .card-title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 15px; font-weight: bold; fill: #1e293b; }
      .txt { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 12px; fill: #334155; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="960" height="600" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />
  
  <text x="480" y="38" text-anchor="middle" class="title">图 1-6 万用表判别半导体器件（二极管与晶体管 3DG / 3CG）极性图解</text>
  <text x="480" y="60" text-anchor="middle" class="sub">机械指针表 vs 数字万用表测试差异、管脚辨识规则与好坏判断标准</text>

  <!-- 上部左侧：指针表 vs 数字表核心差异 -->
  <g transform="translate(40, 85)" filter="url(#shadow)">
    <rect width="430" height="235" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" />
    <text x="20" y="30" class="card-title">1. 万用表面板表笔极性“关键陷阱”</text>

    <!-- 指针表卡片 -->
    <rect x="20" y="48" width="390" height="80" rx="6" fill="#fffbeb" stroke="#fde68a" />
    <text x="32" y="70" font-family="sans-serif" font-weight="bold" font-size="13" fill="#b45309">● 指针式万用表 (电阻挡 R×1kΩ)：</text>
    <text x="32" y="92" class="txt">内部接线特性：<tspan font-weight="bold" fill="#dc2626">黑表笔接内部电池正极(+)</tspan>，<tspan font-weight="bold" fill="#2563eb">红表笔接内部电池负极(-)</tspan>！</text>
    <text x="32" y="112" class="txt">指针偏转角度大（阻值较小几千欧）时，黑表笔所碰引脚即为二极管正极！</text>

    <!-- 数字表卡片 -->
    <rect x="20" y="138" width="390" height="80" rx="6" fill="#eff6ff" stroke="#bfdbfe" />
    <text x="32" y="160" font-family="sans-serif" font-weight="bold" font-size="13" fill="#1d4ed8">● 数字式万用表 (二极管挡)：</text>
    <text x="32" y="182" class="txt">面板与极性一致：<tspan font-weight="bold" fill="#dc2626">红表笔为正极(+)</tspan>，<tspan font-weight="bold" fill="#1e293b">黑表笔为负极(-)</tspan>！</text>
    <text x="32" y="202" class="txt">屏幕直显管压降：硅管显示 0.5~0.7V；锗管显示 0.2~0.3V；反向显示“1”或“OL”。</text>
  </g>

  <!-- 上部右侧：二极管判别流程 -->
  <g transform="translate(490, 85)" filter="url(#shadow)">
    <rect width="430" height="235" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" />
    <text x="20" y="30" class="card-title">2. 二极管极性与好坏判别法则</text>

    <g transform="translate(20, 50)">
      <!-- 正常管子 -->
      <rect width="390" height="50" rx="6" fill="#ecfdf5" stroke="#a7f3d0" />
      <text x="15" y="22" font-size="12" font-weight="bold" fill="#047857">✅ 良好器件：单向导电性良好</text>
      <text x="15" y="40" font-size="11" fill="#065f46">正向导通（电阻小 / 显示 0.7V 压降），反向截止（电阻极大 / 显示 OL）。</text>

      <!-- 损坏管子：击穿短路 -->
      <rect y="58" width="390" height="50" rx="6" fill="#fef2f2" stroke="#fecaca" />
      <text x="15" y="80" font-size="12" font-weight="bold" fill="#b91c1c">❌ 损坏（短路击穿）：</text>
      <text x="15" y="98" font-size="11" fill="#7f1d1d">正向与反向电阻均接近 0Ω，或数字表二极管档发出连续短路蜂鸣。</text>

      <!-- 损坏管子：开路烧断 -->
      <rect y="116" width="390" height="50" rx="6" fill="#fef2f2" stroke="#fecaca" />
      <text x="15" y="138" font-size="12" font-weight="bold" fill="#b91c1c">❌ 损坏（内部开路烧断）：</text>
      <text x="15" y="156" font-size="11" fill="#7f1d1d">正向与反向电阻均为无穷大（∞），器件无法导通，完全失效。</text>
    </g>
  </g>

  <!-- 下部：三极管 3DG (NPN) 与 3CG (PNP) 引脚判定图解 -->
  <g transform="translate(40, 335)" filter="url(#shadow)">
    <rect width="880" height="235" rx="12" fill="#ffffff" stroke="#cbd5e1" stroke-width="2" />
    <text x="20" y="30" class="card-title">3. 晶体三极管 (3DG 型 NPN / 3CG 型 PNP) 引脚判定与金属封装管脚定位</text>

    <!-- 金属外壳 TO-18 视图 -->
    <g transform="translate(50, 55)">
      <circle cx="70" cy="70" r="50" fill="#f1f5f9" stroke="#334155" stroke-width="2.5" />
      <!-- 定位凸起 tab -->
      <rect x="15" y="60" width="10" height="20" rx="2" fill="#334155" />
      <text x="20" y="50" font-size="11" font-weight="bold" fill="#b91c1c">定位凸起</text>
      
      <!-- 三个管脚 -->
      <circle cx="45" cy="70" r="7" fill="#ef4444" /> <!-- e -->
      <text x="45" y="74" text-anchor="middle" font-size="10" fill="#ffffff" font-weight="bold">e</text>

      <circle cx="70" cy="45" r="7" fill="#3b82f6" /> <!-- b -->
      <text x="70" y="49" text-anchor="middle" font-size="10" fill="#ffffff" font-weight="bold">b</text>

      <circle cx="95" cy="70" r="7" fill="#10b981" /> <!-- c -->
      <text x="95" y="74" text-anchor="middle" font-size="10" fill="#ffffff" font-weight="bold">c</text>

      <text x="70" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="#1e293b">TO-18 金属底视图</text>
      <text x="70" y="152" text-anchor="middle" font-size="11" fill="#64748b">紧靠凸起为发射极 e</text>
    </g>

    <!-- 判别三部曲 -->
    <g transform="translate(230, 48)">
      <rect width="620" height="160" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
      
      <text x="20" y="25" font-size="13" font-weight="bold" fill="#1e293b">第一步：找基极 b 与判别管型 (NPN / PNP)</text>
      <text x="20" y="48" class="txt">
        用一块表笔分别去接触另外两脚。若两次测得电阻都很小，则所固定的脚为 <tspan font-weight="bold" fill="#1d4ed8">基极 b</tspan>。
      </text>
      <text x="20" y="66" class="txt">
        ● 若固定的是红表笔（数字表）为公共正极 ➔ <tspan font-weight="bold" fill="#dc2626">NPN 型 (如 3DG6)</tspan>；若固定的是黑表笔为公共负极 ➔ <tspan font-weight="bold" fill="#2563eb">PNP 型 (如 3CG12)</tspan>。
      </text>

      <text x="20" y="95" font-size="13" font-weight="bold" fill="#1e293b">第二步：判定集电极 c 与发射极 e</text>
      <text x="20" y="118" class="txt">
        ● 方法 A（仪表插槽法）：直接插入数字万用表面板上的 <tspan font-weight="bold">hFE</tspan> 测试插孔，读数在几十到几百（正常β值）时，引脚对应完全正确。
      </text>
      <text x="20" y="138" class="txt">
        ● 方法 B（利用放大能力）：手指捏住 b 与假定 c 之间（充当人体偏置电阻），测 ce 间阻值，阻值偏转更明显者假定 c 极正确。
      </text>
    </g>
  </g>
</svg>'''

with open("images/fig6_multimeter_pinout_check.svg", "w", encoding="utf-8") as f:
    f.write(fig6_content)

print("fig6 generated")
