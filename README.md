<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GitHub Banner - Nicolette Mashaba</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            overflow: hidden;
            background: #000;
        }

        .banner-container {
            position: relative;
            width: 100vw;
            height: 100vh;
            background: linear-gradient(135deg, #0a0e27 0%, #1a1f3a 50%, #0f1419 100%);
            overflow: hidden;
        }

        /* Animated Grid Background */
        .grid-background {
            position: absolute;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(rgba(0, 217, 255, 0.1) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 217, 255, 0.1) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: gridMove 20s linear infinite;
            transform: perspective(500px) rotateX(60deg);
            transform-origin: center center;
        }

        @keyframes gridMove {
            0% {
                transform: perspective(500px) rotateX(60deg) translateY(0);
            }
            100% {
                transform: perspective(500px) rotateX(60deg) translateY(50px);
            }
        }

        /* Floating Particles */
        .particles {
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }

        .particle {
            position: absolute;
            background: #00d9ff;
            border-radius: 50%;
            pointer-events: none;
            opacity: 0;
            animation: float 8s infinite ease-in-out;
        }

        @keyframes float {
            0%, 100% {
                opacity: 0;
                transform: translateY(100vh) scale(0);
            }
            10% {
                opacity: 1;
            }
            90% {
                opacity: 1;
            }
            100% {
                transform: translateY(-100px) scale(1);
            }
        }

        /* Neural Network Lines */
        canvas {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        /* Content Container */
        .content {
            position: relative;
            z-index: 10;
            height: 100%;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 40px;
            text-align: center;
        }

        /* Glitch Effect Title */
        .glitch-wrapper {
            position: relative;
            margin-bottom: 20px;
        }

        .glitch {
            font-family: 'Courier New', monospace;
            font-size: clamp(2rem, 6vw, 4rem);
            font-weight: 900;
            color: #00d9ff;
            letter-spacing: 3px;
            text-transform: uppercase;
            position: relative;
            text-shadow: 
                0 0 10px #00d9ff,
                0 0 20px #00d9ff,
                0 0 30px #00d9ff;
            animation: glitch 3s infinite;
        }

        .glitch::before,
        .glitch::after {
            content: attr(data-text);
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
        }

        .glitch::before {
            left: 2px;
            text-shadow: -2px 0 #ff6b35;
            clip: rect(24px, 550px, 90px, 0);
            animation: glitch-anim 2s infinite linear alternate-reverse;
        }

        .glitch::after {
            left: -2px;
            text-shadow: -2px 0 #00d9ff;
            clip: rect(85px, 550px, 140px, 0);
            animation: glitch-anim 3s infinite linear alternate-reverse;
        }

        @keyframes glitch {
            0%, 100% {
                transform: translate(0);
            }
            20% {
                transform: translate(-2px, 2px);
            }
            40% {
                transform: translate(-2px, -2px);
            }
            60% {
                transform: translate(2px, 2px);
            }
            80% {
                transform: translate(2px, -2px);
            }
        }

        @keyframes glitch-anim {
            0% {
                clip: rect(random(100) + px, 9999px, random(100) + px, 0);
            }
            100% {
                clip: rect(random(100) + px, 9999px, random(100) + px, 0);
            }
        }

        /* Subtitle */
        .subtitle {
            font-family: 'Arial', sans-serif;
            font-size: clamp(1rem, 2.5vw, 1.5rem);
            color: #ffffff;
            margin-bottom: 30px;
            opacity: 0;
            animation: fadeInUp 1s ease forwards 0.5s;
        }

        .subtitle span {
            color: #ff6b35;
            font-weight: bold;
        }

        /* Tech Stack Pills */
        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            justify-content: center;
            margin-top: 20px;
            opacity: 0;
            animation: fadeInUp 1s ease forwards 1s;
        }

        .tech-pill {
            background: rgba(0, 217, 255, 0.1);
            border: 2px solid #00d9ff;
            padding: 8px 20px;
            border-radius: 25px;
            color: #00d9ff;
            font-family: 'Courier New', monospace;
            font-size: clamp(0.7rem, 1.5vw, 0.9rem);
            font-weight: bold;
            box-shadow: 0 0 15px rgba(0, 217, 255, 0.3);
            animation: pulse 2s infinite;
            transition: all 0.3s ease;
        }

        .tech-pill:hover {
            background: rgba(0, 217, 255, 0.3);
            transform: scale(1.1);
            box-shadow: 0 0 25px rgba(0, 217, 255, 0.6);
        }

        @keyframes pulse {
            0%, 100% {
                box-shadow: 0 0 15px rgba(0, 217, 255, 0.3);
            }
            50% {
                box-shadow: 0 0 25px rgba(0, 217, 255, 0.6);
            }
        }

        @keyframes fadeInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Code Rain Effect */
        .code-rain {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            overflow: hidden;
        }

        .code-column {
            position: absolute;
            top: -100%;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            color: #00d9ff;
            opacity: 0.3;
            white-space: nowrap;
            animation: rain linear infinite;
        }

        @keyframes rain {
            to {
                top: 100%;
            }
        }

        /* Scanning Line */
        .scan-line {
            position: absolute;
            width: 100%;
            height: 2px;
            background: linear-gradient(90deg, transparent, #00d9ff, transparent);
            animation: scan 3s linear infinite;
            box-shadow: 0 0 10px #00d9ff;
        }

        @keyframes scan {
            from {
                top: 0;
            }
            to {
                top: 100%;
            }
        }
    </style>
</head>
<body>
    <div class="banner-container">
        <!-- Grid Background -->
        <div class="grid-background"></div>

        <!-- Neural Network Canvas -->
        <canvas id="neuralCanvas"></canvas>

        <!-- Particles -->
        <div class="particles" id="particles"></div>

        <!-- Code Rain -->
        <div class="code-rain" id="codeRain"></div>

        <!-- Scanning Line -->
        <div class="scan-line"></div>

        <!-- Main Content -->
        <div class="content">
            <div class="glitch-wrapper">
                <h1 class="glitch" data-text="NICOLETTE MASHABA">NICOLETTE MASHABA</h1>
            </div>
            <p class="subtitle">
                <span>AI/ML Engineer</span> | Software Developer | <span>DevOps Specialist</span>
            </p>
            <div class="tech-stack">
                <div class="tech-pill">🤖 AI/ML</div>
                <div class="tech-pill">🚀 DevOps</div>
                <div class="tech-pill">☁️ Azure Cloud</div>
                <div class="tech-pill">⚡ React</div>
                <div class="tech-pill">🐍 Python</div>
                <div class="tech-pill">🔷 C#/.NET</div>
            </div>
        </div>
    </div>

    <script>
        // Neural Network Animation
        const canvas = document.getElementById('neuralCanvas');
        const ctx = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;

        const nodes = [];
        const nodeCount = 50;

        class Node {
            constructor() {
                this.x = Math.random() * canvas.width;
                this.y = Math.random() * canvas.height;
                this.vx = (Math.random() - 0.5) * 0.5;
                this.vy = (Math.random() - 0.5) * 0.5;
                this.radius = Math.random() * 2 + 1;
            }

            update() {
                this.x += this.vx;
                this.y += this.vy;

                if (this.x < 0 || this.x > canvas.width) this.vx *= -1;
                if (this.y < 0 || this.y > canvas.height) this.vy *= -1;
            }

            draw() {
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.radius, 0, Math.PI * 2);
                ctx.fillStyle = '#00d9ff';
                ctx.fill();
            }
        }

        for (let i = 0; i < nodeCount; i++) {
            nodes.push(new Node());
        }

        function drawConnections() {
            for (let i = 0; i < nodes.length; i++) {
                for (let j = i + 1; j < nodes.length; j++) {
                    const dx = nodes[i].x - nodes[j].x;
                    const dy = nodes[i].y - nodes[j].y;
                    const distance = Math.sqrt(dx * dx + dy * dy);

                    if (distance < 150) {
                        ctx.beginPath();
                        ctx.moveTo(nodes[i].x, nodes[i].y);
                        ctx.lineTo(nodes[j].x, nodes[j].y);
                        ctx.strokeStyle = `rgba(0, 217, 255, ${1 - distance / 150})`;
                        ctx.lineWidth = 0.5;
                        ctx.stroke();
                    }
                }
            }
        }

        function animate() {
            ctx.fillStyle = 'rgba(10, 14, 39, 0.1)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            nodes.forEach(node => {
                node.update();
                node.draw();
            });

            drawConnections();
            requestAnimationFrame(animate);
        }

        animate();

        // Floating Particles
        const particlesContainer = document.getElementById('particles');
        for (let i = 0; i < 30; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.width = Math.random() * 4 + 2 + 'px';
            particle.style.height = particle.style.width;
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 8 + 's';
            particle.style.animationDuration = Math.random() * 5 + 8 + 's';
            particlesContainer.appendChild(particle);
        }

        // Code Rain Effect
        const codeRain = document.getElementById('codeRain');
        const codeChars = 'AIMLPythonReactAzureKubernetesDockerTensorFlowPyTorch01';
        
        for (let i = 0; i < 15; i++) {
            const column = document.createElement('div');
            column.className = 'code-column';
            column.style.left = Math.random() * 100 + '%';
            column.style.animationDuration = Math.random() * 5 + 10 + 's';
            column.style.animationDelay = Math.random() * 5 + 's';
            
            let text = '';
            for (let j = 0; j < 20; j++) {
                text += codeChars[Math.floor(Math.random() * codeChars.length)] + '<br>';
            }
            column.innerHTML = text;
            codeRain.appendChild(column);
        }

        // Resize canvas on window resize
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });
    </script>
</body>
</html>
