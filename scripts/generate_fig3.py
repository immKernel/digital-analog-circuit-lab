# -*- coding: utf-8 -*-
import os

os.makedirs("images", exist_ok=True)

# 3. Waveform Troubleshooting SVG (Fig 1-3 from manual)
fig3_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 680" width="100%" height="100%">
  <defs>
    <style>
      .main-title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 20px; font-weight: bold; fill: #0f172a; }
      .main-sub { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 13px; fill: #64748b; }
      .case-title { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 14px; font-weight: bold; fill: #1e293b; }
      .reason-text { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 12px; fill: #b91c1c; }
      .solution-text { font-family: system-ui, -apple-system, 'Microsoft YaHei', sans-serif; font-size: 12px; fill: #047857; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <rect width="1000" height="680" rx="16" fill="#f8fafc" stroke="#e2e8f0" stroke-width="2" />
  
  <text x="500" y="38" text-anchor="middle" class="main-title">图 1-3 示波器观察正弦信号常见异常波形图解与调节排除秘籍（对应指导书思考题）</text>
  <text x="500" y="60" text-anchor="middle" class="main-sub">掌握 8 种典型异常波形的成因诊断与旋钮调节方法，快速获得规范标准波形</text>

  <!-- 8 个卡片，4列 2行 -->
  <!-- 行1: y=80; 行2: y=380 -->
  <!-- 列宽: 215px, 间距: 20px, x起始: 35px -->

  <!-- Case A: 仅有一点或垂直线 -->
  <g transform="translate(35, 80)" filter="url(#shadow)">
    <rect width="215" height="280" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
    <rect x="15" y="15" width="185" height="120" rx="6" fill="#0f172a" />
    <!-- 荧光屏网格微弱 -->
    <line x1="15" y1="75" x2="200" y2="75" stroke="#047857" stroke-dasharray="2,2" />
    <line x1="107" y1="15" x2="107" y2="135" stroke="#047857" stroke-dasharray="2,2" />
    <!-- 仅一个光斑点或一条垂直线 -->
    <circle cx="107" cy="75" r="4" fill="#34d399" filter="drop-shadow(0 0 3px #10b981)" />
    <line x1="107" y1="45" x2="107" y2="105" stroke="#34d399" stroke-width="2.5" opacity="0.6" />
    
    <text x="15" y="155" class="case-title">情景 (a)：仅有一个光点/垂直线</text>
    <text x="15" y="180" class="reason-text">❌ 故障原因：</text>
    <text x="15" y="198" font-size="11" fill="#334155" font-family="sans-serif">扫描处于关闭或 X-Y 模式；未开启内部水平时基扫描。</text>
    <text x="15" y="230" class="solution-text">✅ 排除方法：</text>
    <text x="15" y="248" font-size="11" fill="#334155" font-family="sans-serif">调节 Time/div 切出 X-Y 档；触发模式置于“AUTO”自激状态。</text>
  </g>

  <!-- Case B: 波形严重偏离屏幕中心 -->
  <g transform="translate(275, 80)" filter="url(#shadow)">
    <rect width="215" height="280" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
    <rect x="15" y="15" width="185" height="120" rx="6" fill="#0f172a" />
    <line x1="15" y1="75" x2="200" y2="75" stroke="#047857" stroke-dasharray="2,2" />
    <line x1="107" y1="15" x2="107" y2="135" stroke="#047857" stroke-dasharray="2,2" />
    <!-- 偏向右上角的波形 -->
    <path d="M 25 35 Q 55 15, 85 35 T 145 35 T 200 35" fill="none" stroke="#34d399" stroke-width="2" />
    
    <text x="15" y="155" class="case-title">情景 (b)：波形严重偏离中央</text>
    <text x="15" y="180" class="reason-text">❌ 故障原因：</text>
    <text x="15" y="198" font-size="11" fill="#334155" font-family="sans-serif">垂直 Y 或水平 X 位移旋钮偏置；输入含有过大直流偏置。</text>
    <text x="15" y="230" class="solution-text">✅ 排除方法：</text>
    <text x="15" y="248" font-size="11" fill="#334155" font-family="sans-serif">调节 Y-POS 和 X-POS 居中；耦合开关切至“AC”阻隔直流。</text>
  </g>

  <!-- Case C: 垂直幅度极小 -->
  <g transform="translate(515, 80)" filter="url(#shadow)">
    <rect width="215" height="280" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
    <rect x="15" y="15" width="185" height="120" rx="6" fill="#0f172a" />
    <line x1="15" y1="75" x2="200" y2="75" stroke="#047857" stroke-dasharray="2,2" />
    <line x1="107" y1="15" x2="107" y2="135" stroke="#047857" stroke-dasharray="2,2" />
    <!-- 极其扁平的波形 -->
    <path d="M 20 75 Q 40 70, 60 75 T 100 75 T 140 75 T 180 75 T 200 75" fill="none" stroke="#34d399" stroke-width="2" />
    
    <text x="15" y="155" class="case-title">情景 (c)：垂直幅度极小扁平</text>
    <text x="15" y="180" class="reason-text">❌ 故障原因：</text>
    <text x="15" y="198" font-size="11" fill="#334155" font-family="sans-serif">Y 轴衰减开关 Volts/div 档位选择过大；或探头打在 10X 档未放大。</text>
    <text x="15" y="230" class="solution-text">✅ 排除方法：</text>
    <text x="15" y="248" font-size="11" fill="#334155" font-family="sans-serif">逆时针调小 Volts/div 档位（如从 5V/div 调至 0.5V/div）。</text>
  </g>

  <!-- Case D: 水平方向波形极密 -->
  <g transform="translate(755, 80)" filter="url(#shadow)">
    <rect width="215" height="280" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
    <rect x="15" y="15" width="185" height="120" rx="6" fill="#0f172a" />
    <line x1="15" y1="75" x2="200" y2="75" stroke="#047857" stroke-dasharray="2,2" />
    <line x1="107" y1="15" x2="107" y2="135" stroke="#047857" stroke-dasharray="2,2" />
    <!-- 极其密集的波形 -->
    <path d="M 20 75 Q 25 45, 30 75 T 40 75 T 50 75 T 60 75 T 70 75 T 80 75 T 90 75 T 100 75 T 110 75 T 120 75 T 130 75 T 140 75 T 150 75 T 160 75 T 170 75 T 180 75 T 190 75 T 200 75" fill="none" stroke="#34d399" stroke-width="1.5" />
    
    <text x="15" y="155" class="case-title">情景 (d)：波形密集如光带</text>
    <text x="15" y="180" class="reason-text">❌ 故障原因：</text>
    <text x="15" y="198" font-size="11" fill="#334155" font-family="sans-serif">扫描时基 Time/div 档位过大，单屏内容纳过多周期波形。</text>
    <text x="15" y="230" class="solution-text">✅ 排除方法：</text>
    <text x="15" y="248" font-size="11" fill="#334155" font-family="sans-serif">顺时针调小 Time/div（例如从 10ms/div 调至 0.2ms/div）。</text>
  </g>

  <!-- 行 2 -->
  <!-- Case E: 周期过少/拉伸过宽 -->
  <g transform="translate(35, 380)" filter="url(#shadow)">
    <rect width="215" height="280" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
    <rect x="15" y="15" width="185" height="120" rx="6" fill="#0f172a" />
    <line x1="15" y1="75" x2="200" y2="75" stroke="#047857" stroke-dasharray="2,2" />
    <line x1="107" y1="15" x2="107" y2="135" stroke="#047857" stroke-dasharray="2,2" />
    <!-- 仅半个周期拉伸 -->
    <path d="M 20 75 Q 107 10, 200 75" fill="none" stroke="#34d399" stroke-width="2.5" />
    
    <text x="15" y="155" class="case-title">情景 (e)：波形过宽不完整</text>
    <text x="15" y="180" class="reason-text">❌ 故障原因：</text>
    <text x="15" y="198" font-size="11" fill="#334155" font-family="sans-serif">扫描时基 Time/div 档位过小，扫描速率过快，单屏不满一周期。</text>
    <text x="15" y="230" class="solution-text">✅ 排除方法：</text>
    <text x="15" y="248" font-size="11" fill="#334155" font-family="sans-serif">逆时针增大 Time/div 档位，使屏幕完整展现 2~3 个周期。</text>
  </g>

  <!-- Case F: 双重波形/左右晃动跑动 -->
  <g transform="translate(275, 380)" filter="url(#shadow)">
    <rect width="215" height="280" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
    <rect x="15" y="15" width="185" height="120" rx="6" fill="#0f172a" />
    <line x1="15" y1="75" x2="200" y2="75" stroke="#047857" stroke-dasharray="2,2" />
    <line x1="107" y1="15" x2="107" y2="135" stroke="#047857" stroke-dasharray="2,2" />
    <!-- 重叠交错虚影 -->
    <path d="M 20 75 Q 60 25, 107 75 T 195 75" fill="none" stroke="#34d399" stroke-width="2" opacity="0.9" />
    <path d="M 35 75 Q 75 35, 122 75 T 200 75" fill="none" stroke="#34d399" stroke-width="1.8" opacity="0.5" stroke-dasharray="4,2" />
    
    <text x="15" y="155" class="case-title">情景 (f)：双影重叠/左右滚动</text>
    <text x="15" y="180" class="reason-text">❌ 故障原因：</text>
    <text x="15" y="198" font-size="11" fill="#334155" font-family="sans-serif">触发电平 Trigger Level 设置偏移未触碰信号；触发源选择错误。</text>
    <text x="15" y="230" class="solution-text">✅ 排除方法：</text>
    <text x="15" y="248" font-size="11" fill="#334155" font-family="sans-serif">旋转 Level 旋钮直至锁定；确认触发源设为被测通道 (CH1/CH2)。</text>
  </g>

  <!-- Case G: 波形顶部/底部平头失真 -->
  <g transform="translate(515, 380)" filter="url(#shadow)">
    <rect width="215" height="280" rx="10" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" />
    <rect x="15" y="15" width="185" height="120" rx="6" fill="#0f172a" />
    <line x1="15" y1="75" x2="200" y2="75" stroke="#047857" stroke-dasharray="2,2" />
    <line x1="107" y1="15" x2="107" y2="135" stroke="#047857" stroke-dasharray="2,2" />
    <!-- 削顶削底失真波形 -->
    <path d="M 20 75 L 40 40 L 70 40 L 90 75 L 110 110 L 140 110 L 160 75 T 200 75" fill="none" stroke="#f43f5e" stroke-width="2" />
    
    <text x="15" y="155" class="case-title">情景 (g)：削顶/削底平头失真</text>
    <text x="15" y="180" class="reason-text">❌ 故障原因：</text>
    <text x="15" y="198" font-size="11" fill="#334155" font-family="sans-serif">信号源输入幅度过大超过运放/示波器线性范围；或静态工作点偏移。</text>
    <text x="15" y="230" class="solution-text">✅ 排除方法：</text>
    <text x="15" y="248" font-size="11" fill="#334155" font-family="sans-serif">调小信号发生器输出幅度；在信号源端按下 20dB/40dB 衰减键。</text>
  </g>

  <!-- Case H: 标准理想规范波形 -->
  <g transform="translate(755, 380)" filter="url(#shadow)">
    <rect width="215" height="280" rx="10" fill="#ecfdf5" stroke="#10b981" stroke-width="2" />
    <rect x="15" y="15" width="185" height="120" rx="6" fill="#064e3b" />
    <line x1="15" y1="75" x2="200" y2="75" stroke="#047857" stroke-width="1.5" stroke-dasharray="2,2" />
    <line x1="107" y1="15" x2="107" y2="135" stroke="#047857" stroke-width="1.5" stroke-dasharray="2,2" />
    <!-- 完美居中 2 个周期正弦波 -->
    <path d="M 20 75 Q 42 30, 65 75 T 110 75 Q 132 30, 155 75 T 200 75" fill="none" stroke="#34d399" stroke-width="2.5" />
    
    <text x="15" y="155" class="case-title" fill="#047857">✨ 标准规范状态 (达成！)</text>
    <text x="15" y="180" font-weight="bold" font-size="12" fill="#059669">🏆 实验报告规范要求：</text>
    <text x="15" y="200" font-size="11" fill="#334155" font-family="sans-serif">1. 完整展现 2~3 个周期波形</text>
    <text x="15" y="218" font-size="11" fill="#334155" font-family="sans-serif">2. 垂直占屏 1/2 到 2/3 (防失真)</text>
    <text x="15" y="236" font-size="11" fill="#334155" font-family="sans-serif">3. 辉度聚焦适中，线条最细清晰</text>
    <text x="15" y="254" font-size="11" fill="#334155" font-family="sans-serif">4. 微调 CAL 旋至校正档保读数</text>
  </g>
</svg>'''

with open("images/fig3_waveform_troubleshooting.svg", "w", encoding="utf-8") as f:
    f.write(fig3_content)

print("fig3 generated")
