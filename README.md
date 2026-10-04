<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Sistemas Distribuidos | Portafolio</title>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: "Inter", sans-serif;
            background: #020617;
            color: white;
            overflow-x: hidden;
        }

        /* =========================
           FONDO FUTURISTA
        ========================== */

        body::before {
            content: "";
            position: fixed;
            inset: 0;
            background:
                linear-gradient(rgba(2, 6, 23, .75), rgba(2, 6, 23, .92)),
                url("https://images.unsplash.com/photo-1451187580459-43490279c0fa?auto=format&fit=crop&w=2400&q=90")
                center / cover no-repeat;
            z-index: -3;
        }

        body::after {
            content: "";
            position: fixed;
            inset: 0;
            background:
                radial-gradient(circle at 20% 20%, rgba(0, 200, 255, .18), transparent 30%),
                radial-gradient(circle at 80% 70%, rgba(0, 255, 170, .12), transparent 30%);
            z-index: -2;
            pointer-events: none;
        }

        /* =========================
           PARTICULAS
        ========================== */

        .particles {
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: -1;
            overflow: hidden;
        }

        .particle {
            position: absolute;
            width: 3px;
            height: 3px;
            background: #00eaff;
            border-radius: 50%;
            box-shadow: 0 0 12px #00eaff;
            animation: float linear infinite;
        }

        .particle:nth-child(1) {
            left: 10%;
            animation-duration: 12s;
            top: 100%;
        }

        .particle:nth-child(2) {
            left: 25%;
            animation-duration: 18s;
            top: 100%;
        }

        .particle:nth-child(3) {
            left: 40%;
            animation-duration: 14s;
            top: 100%;
        }

        .particle:nth-child(4) {
            left: 60%;
            animation-duration: 20s;
            top: 100%;
        }

        .particle:nth-child(5) {
            left: 75%;
            animation-duration: 15s;
            top: 100%;
        }

        .particle:nth-child(6) {
            left: 90%;
            animation-duration: 17s;
            top: 100%;
        }

        @keyframes float {
            from {
                transform: translateY(0);
                opacity: 0;
            }

            20% {
                opacity: 1;
            }

            to {
                transform: translateY(-120vh);
                opacity: 0;
            }
        }

        /* =========================
           NAVBAR
        ========================== */

        nav {
            position: fixed;
            top: 0;
            width: 100%;
            padding: 22px 7%;
            display: flex;
            justify-content: space-between;
            align-items: center;
            backdrop-filter: blur(15px);
            background: rgba(2, 6, 23, .55);
            border-bottom: 1px solid rgba(0, 234, 255, .15);
            z-index: 100;
        }

        .logo {
            font-family: "Orbitron", sans-serif;
            font-weight: 700;
            letter-spacing: 2px;
            color: #fff;
        }

        .logo span {
            color: #00eaff;
        }

        nav a {
            color: #cbd5e1;
            text-decoration: none;
            margin-left: 30px;
            font-size: 14px;
            transition: .3s;
        }

        nav a:hover {
            color: #00eaff;
            text-shadow: 0 0 10px #00eaff;
        }

        /* =========================
           HERO
        ========================== */

        .hero {
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 100px 20px 60px;
        }

        .hero-content {
            max-width: 1000px;
        }

        .badge {
            display: inline-block;
            padding: 10px 20px;
            border: 1px solid rgba(0, 234, 255, .4);
            border-radius: 50px;
            color: #00eaff;
            background: rgba(0, 234, 255, .07);
            font-size: 13px;
            letter-spacing: 2px;
            margin-bottom: 30px;
            animation: pulse 2.5s infinite;
        }

        @keyframes pulse {
            0%, 100% {
                box-shadow: 0 0 0 rgba(0, 234, 255, 0);
            }

            50% {
                box-shadow: 0 0 30px rgba(0, 234, 255, .18);
            }
        }

        h1 {
            font-family: "Orbitron", sans-serif;
            font-size: clamp(45px, 8vw, 95px);
            line-height: 1;
            margin-bottom: 25px;
            letter-spacing: -2px;
        }

        h1 .blue {
            color: #00eaff;
            text-shadow:
                0 0 15px rgba(0, 234, 255, .7),
                0 0 50px rgba(0, 234, 255, .3);
        }

        .subtitle {
            font-size: clamp(18px, 3vw, 27px);
            color: #cbd5e1;
            margin-bottom: 20px;
        }

        .description {
            max-width: 720px;
            margin: auto;
            color: #94a3b8;
            line-height: 1.8;
            font-size: 16px;
        }

        /* =========================
           BOTONES
        ========================== */

        .buttons {
            margin-top: 40px;
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }

        .btn {
            text-decoration: none;
            padding: 15px 28px;
            border-radius: 8px;
            font-weight: 600;
            transition: .3s;
        }

        .btn-primary {
            background: #00eaff;
            color: #020617;
            box-shadow: 0 0 25px rgba(0, 234, 255, .3);
        }

        .btn-primary:hover {
            transform: translateY(-4px);
            box-shadow: 0 0 40px rgba(0, 234, 255, .6);
        }

        .btn-secondary {
            border: 1px solid rgba(255,255,255,.2);
            color: white;
            background: rgba(255,255,255,.05);
            backdrop-filter: blur(10px);
        }

        .btn-secondary:hover {
            border-color: #00eaff;
            color: #00eaff;
            transform: translateY(-4px);
        }

        /* =========================
           INFORMACION
        ========================== */

        .section {
            padding: 100px 7%;
        }

        .section-title {
            text-align: center;
            font-family: "Orbitron", sans-serif;
            font-size: 35px;
            margin-bottom: 60px;
        }

        .section-title span {
            color: #00eaff;
        }

        .cards {
            max-width: 1100px;
            margin: auto;
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 25px;
        }

        .card {
            padding: 35px 25px;
            background: rgba(15, 23, 42, .65);
            border: 1px solid rgba(255,255,255,.08);
            border-radius: 18px;
            backdrop-filter: blur(15px);
            transition: .4s;
            position: relative;
            overflow: hidden;
        }

        .card::before {
            content: "";
            position: absolute;
            width: 100px;
            height: 100px;
            background: #00eaff;
            filter: blur(70px);
            opacity: .08;
            top: -40px;
            right: -40px;
        }

        .card:hover {
            transform: translateY(-10px);
            border-color: rgba(0, 234, 255, .5);
            box-shadow: 0 15px 50px rgba(0,0,0,.4);
        }

        .icon {
            font-size: 40px;
            margin-bottom: 20px;
        }

        .card h3 {
            font-family: "Orbitron", sans-serif;
            margin-bottom: 15px;
            font-size: 19px;
        }

        .card p {
            color: #94a3b8;
            line-height: 1.7;
            font-size: 14px;
        }

        /* =========================
           TECNOLOGIAS
        ========================== */

        .tech {
            max-width: 900px;
            margin: auto;
            display: flex;
            justify-content: center;
            gap: 15px;
            flex-wrap: wrap;
        }

        .tech span {
            padding: 12px 20px;
            border-radius: 8px;
            background: rgba(0,234,255,.06);
            border: 1px solid rgba(0,234,255,.2);
            color: #cbd5e1;
            transition: .3s;
        }

        .tech span:hover {
            color: #00eaff;
            border-color: #00eaff;
            box-shadow: 0 0 20px rgba(0,234,255,.2);
            transform: scale(1.05);
        }

        /* =========================
           FOOTER
        ========================== */

        footer {
            text-align: center;
            padding: 40px 20px;
            border-top: 1px solid rgba(255,255,255,.08);
            color: #64748b;
            font-size: 14px;
        }

        footer strong {
            color: #00eaff;
        }

        /* =========================
           RESPONSIVE
        ========================== */

        @media (max-width: 800px) {

            nav {
                padding: 18px 5%;
            }

            nav div:last-child {
                display: none;
            }

            .cards {
                grid-template-columns: 1fr;
            }

            .section {
                padding: 70px 6%;
            }

            h1 {
                font-size: 48px;
            }
        }

    </style>
</head>

<body>

    <!-- Partículas -->
    <div class="particles">
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
        <div class="particle"></div>
    </div>

    <!-- NAVBAR -->
    <nav>
        <div class="logo">
            SD<span>//</span>2026
        </div>

        <div>
            <a href="#inicio">Inicio</a>
            <a href="#contenido">Contenido</a>
            <a href="#tecnologias">Tecnologías</a>
        </div>
    </nav>

    <!-- HERO -->
    <section class="hero" id="inicio">

        <div class="hero-content">

            <div class="badge">
                UNIVERSIDAD NACIONAL DE LOJA · 2026
            </div>

            <h1>
                SISTEMAS<br>
                <span class="blue">DISTRIBUIDOS</span>
            </h1>

            <p class="subtitle">
                Portafolio Académico
            </p>

            <p class="description">
                Repositorio académico dedicado al estudio de arquitecturas
                distribuidas, comunicación entre procesos, sistemas cliente-servidor,
                middleware, computación en la nube y tecnologías modernas de
                sistemas distribuidos.
            </p>

            <div class="buttons">

                <a href="#contenido" class="btn btn-primary">
                    Explorar repositorio
                </a>

                <a href="#tecnologias" class="btn btn-secondary">
                    Ver tecnologías
                </a>

            </div>

        </div>

    </section>

    <!-- CONTENIDO -->
    <section class="section" id="contenido">

        <h2 class="section-title">
            Áreas de <span>Estudio</span>
        </h2>

        <div class="cards">

            <div class="card">
                <div class="icon">🌐</div>

                <h3>Arquitecturas</h3>

                <p>
                    Análisis de arquitecturas cliente-servidor,
                    sistemas P2P, arquitecturas distribuidas y
                    modelos de comunicación.
                </p>
            </div>

            <div class="card">
                <div class="icon">⚡</div>

                <h3>Comunicación</h3>

                <p>
                    Estudio de protocolos, intercambio de mensajes,
                    comunicación entre procesos y mecanismos de
                    sincronización.
                </p>
            </div>

            <div class="card">
                <div class="icon">☁️</div>

                <h3>Computación</h3>

                <p>
                    Conceptos relacionados con computación en la nube,
                    servicios distribuidos, escalabilidad y
                    disponibilidad.
                </p>
            </div>

        </div>

    </section>

    <!-- TECNOLOGÍAS -->
    <section class="section" id="tecnologias">

        <h2 class="section-title">
            Tecnologías y <span>Conceptos</span>
        </h2>

        <div class="tech">

            <span>Client / Server</span>
            <span>TCP/IP</span>
            <span>HTTP</span>
            <span>REST API</span>
            <span>MQTT</span>
            <span>Docker</span>
            <span>Cloud Computing</span>
            <span>Microservicios</span>
            <span>Middleware</span>
            <span>RPC</span>
            <span>Git</span>
            <span>Python</span>

        </div>

    </section>

    <!-- FOOTER -->
    <footer>

        <p>
            Sistemas Distribuidos ·
            <strong>Portafolio Académico</strong>
        </p>

        <p style="margin-top:10px;">
            Universidad Nacional de Loja · Carrera de Computación
        </p>

    </footer>

</body>
</html>
