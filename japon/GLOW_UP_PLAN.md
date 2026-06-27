# Plan de Glow Up · "Crónica de un viaje anunciado" · v2 Next-Gen

> **Objetivo**: Llevar el proyecto de su estado actual (correcto, bonito, cuidado) a una experiencia **inmersiva, hiperrealista y única** — un regalo digital que se siente como abrir una carta física de otra época, pero con alma de interfaz del futuro.

---

## 0 · Diagnóstico del estado actual

**Lo que hay y funciona bien** (no romper):
- Paleta de papel crema + bermellón + oro + tinta (`#F4ECE0 / #C8382A / #B8893E / #1A1612`) — sofisticada, honesta, atemporal.
- Sistema tipográfico coherente: Cormorant Garamond/Infant (cuerpo), Great Vibes (manuscrita), Inter (UI).
- Flujo narrativo excelente: postal → 7 preguntas → actos con foto → mapa → despedida.
- Transiciones entre nodos geográficos con línea SVG animada.
- Mapa de Japón real con silueta correcta del archipiélago y conexiones.
- Capa de accesibilidad decente: `prefers-reduced-motion`, focus traps, skip link, ARIA labels.
- Datos del viaje están cuidados y el contenido emocional es fuerte.

**Lo que falta para el x100**:
- ❌ Sistema de partículas / atmósfera (no hay vida ambiental).
- ❌ Reveals hiperrealistas (las entradas son fades simples).
- ❌ Pincel / escritura de kanji como elemento narrativo (sólo aparece `旅` estático en sello y `行` enorme de fondo en transición).
- ❌ Personalidad de marca tipográfica — la Great Vibes queda algo "wedding" genérica.
- ❌ Capa háptica visual: tilt 3D en polaroids, micro-parallax, sombras reactivas.
- ❌ Estado "postal" es un componente estático — debería comportarse como un **objeto físico que se abre**.
- ❌ Las fotos de los actos no se sienten únicas — son `<img>` rectangulares con rotación, sin revelado cinematográfico.
- ❌ El mapa pergamino, aunque bonito, no recompensa el scroll ni se siente vivo.
- ❌ La despedida es correcta pero plana — debería ser el clímax emocional.

---

## 0.5 · REGLA ABSOLUTA: mobile-inmersivo primero

> **Noelia va a abrir esto en su iPhone, probablemente tumbada en el sofá, con una mano.** Eso es el 90% del contexto de uso. La versión de escritorio es bonus.

**Principio**: toda interacción que requiera gesto humano debe ser **tap, scroll, swipe o auto-play**. Nada espera a `:hover`. Nada espera al cursor.

**Tabla de gestos canónicos en este proyecto**:

| Gesto | Acción |
|---|---|
| Tap en opción | Selecciona, muestra pensamiento |
| Tap en "comienza el viaje" | Abre sobre, saca postal |
| Tap en pensamiento | Avanza a primer acto |
| Tap en "siguiente →" | Avanza al siguiente acto o pregunta |
| Tap en topbar "volver" | Regresa al inicio |
| Tap en foto | Lightbox |
| Scroll vertical | (limitado — la mayoría del contenido cabe en pantalla) |
| Swipe horizontal en acto | Navegar entre actos del mismo nodo (sólo si hay varios) |
| Auto-play | TODA animación se inicia sola al cargar el estado |

**Lo que se auto-play sin esperar nada**:
- Pétalos de sakura cuando se entra al estado (4s burst).
- Pincelada de kanji cuando se entra a la transición.
- Reveal de polaroid cuando aparece el acto.
- Letter-by-letter de títulos.
- Estampación de sellos.

**Lo que sí depende de tap**:
- Selección de opciones.
- Avanzar entre estados.

**Lo que se reemplaza del plan original** (porque era hover-only):

| Hover-only original | Reemplazo mobile-first |
|---|---|
| Tilt 3D en polaroid | Auto-play tilt oscilante al cargar (`photoSway`) |
| Hover elevación en opciones | Pulso de atención al cargar (scale 1 → 1.02 → 1 una vez) |
| Micro-stamp en hover de CTA | Estampación automática al tap (al click ya hay feedback háptico del SO) |
| Tooltip "relee la carta" en topbar | Texto permanente abajo del brand o no tooltip |
| Shimmer en botón | Shimmer una sola vez al cargar, no en hover |
| Cursor personalizado | **Eliminado** |

**Device-tilt como bonus desktop+** (opcional):
Si `DeviceOrientationEvent` está disponible, el pergamino del mapa se inclina ligeramente según la inclinación del móvil. Esto da una capa háptica sin requerir tap. Se desactiva con `prefers-reduced-motion`.

---

## 1 · Concepto creativo (la dirección)

**Nombre código interno**: **"Bunri" 分离** — la separación que importa: la del papel cuando se abre.

**Tono**: Wabi-sabi premium. Lujo silencioso japonés. Cada elemento tiene textura, peso y movimiento intencional. Nada brilla por brillar; **todo respira**.

**Referencias estéticas que importan** (no copiar, absorber):
- Editorialidad de revistas japonesas (Brutus, Popeye, Ginza) — tipografía grande que respira.
- Ukiyo-e con desplazamiento de capas (efecto "papeles superpuestos", no planos).
- Reservaciones Michelin japonesas: caja negra con un kanji dorado en el sello.
- Apple "spatial UI" pero traducido a Japón: cristal real, profundidad real.
- Cine de Yasujirō Ozu: tatami horizontal, quietud que esconde emoción.

**Lo que NO vamos a hacer** (anti-patterns):
- ❌ Gradientes neón estilo Vaporwave (no es el tono).
- ❌ Dark mode forzado (la experiencia pide papel, no pantalla).
- ❌ Emoji como iconos (sólo SVG, sellos y kanji).
- ❌ Animaciones lineales (todo con curvas Bezier intencionales).
- ❌ Tailwind defaults (este es un proyecto de autor, hecho a medida).
- ❌ Glitch / CRT / vapor (no es nostálgico moderno, es nostálgico **real**).

---

## 2 · Sistema visual refinado

### 2.1 Paleta evolucionada

```css
:root {
  /* — TIERRA (base, ya existía, refinado) — */
  --paper:        #F4ECE0;   /* fondo principal */
  --paper-deep:   #E8DCC4;   /* fondo profundo */
  --paper-shade:  #D6C5A1;   /* sombras suaves */
  --ink:          #1A1612;   /* texto principal */
  --ink-soft:     #4A3F33;   /* texto secundario */
  --ink-mute:     #7A6A5A;   /* texto auxiliar */
  --vermilion:    #C8382A;   /* acento principal (sello) */
  --vermilion-deep: #9B2820; /* acento profundo */
  --gold:         #B8893E;   /* dorado cálido */
  --gold-pale:    #E8C788;   /* dorado claro para highlight */

  /* — NUEVOS TOKENS ATMOSFÉRICOS — */
  --sakura:       #F2C7C7;   /* pétalo claro */
  --sakura-bright:#FFB7C5;   /* pétalo brillante */
  --sakura-pale:  #FFE4E8;   /* pétalo casi blanco */
  --sakura-shadow:#D8A0A8;   /* pétalo en sombra */
  --sumi:         #2A2520;   /* tinta china pura */
  --fuji-blue:    #6B7A8F;   /* azul Monte Fuji al amanecer */
  --fuji-pink:    #F4B6C2;   /* Fuji al atardecer */
  --moss:         #5C6E48;   /* musgo santuario */
  --gold-glow:    #FFD89E;   /* dorado luminoso (sellos, sellos brillantes) */
}
```

### 2.2 Tipografía evolucionada

Sustituciones y adiciones:

| Función | Antes | Después | Por qué |
|---|---|---|---|
| Manoscrita romántica | Great Vibes | **Cormorant Infant Italic 500** | Menos "wedding", más editorial |
| Manoscrita personal "firma" | — | **Caveat** (nueva) | Para la despedida final, más cálida que Great Vibes |
| Serif cuerpo | Cormorant Garamond | Cormorant Garamond *(mantener)* | Ya perfecta |
| Sans UI | Inter | Inter *(mantener)* | Ya perfecta |
| Kanji display | (estático) | **Shippori Mincho B1** 900 | Kanji pincelada serif con peso |
| Kanji cuerpo | (no había) | **Noto Serif JP** 400/700 | Legibilidad para microtextos |
| Japonesa display | — | **Zen Antique / Klee One** | Alternativa pincelada para acentos |

**Importar** (añadir a `<head>`):
```html
<link href="https://fonts.googleapis.com/css2?family=Shippori+Mincho+B1:wght@400;600;800&family=Noto+Serif+JP:wght@300;400;500;700&family=Caveat:wght@400;600&display=swap" rel="stylesheet">
```

### 2.3 Sistema de elevación (3D real)

```css
/* Capas Z explícitas — Japón es profundidad */
--z-base:        0;    /* contenido normal */
--z-paper:       1;    /* capas de papel */
--z-photo:       10;   /* polaroids */
--z-content:     20;   /* texto principal */
--z-nav:         100;  /* topbar */
--z-lightbox:    5000; /* lightbox */
--z-kanji-bg:    100;  /* kanji pincelada grande */
--z-particles:   200;  /* partículas sakura */
--z-cursor:      9999; /* cursor custom */
```

### 2.4 Sistema de sombras físico

Sustituir las `box-shadow` actuales por un sistema **multi-capa que se ve físico**:

```css
/* Polaroid (foto) */
--shadow-photo:
  0 1px 2px rgba(26,22,18,.08),
  0 4px 8px rgba(26,22,18,.10),
  0 12px 24px -4px rgba(26,22,18,.18),
  0 24px 48px -12px rgba(26,22,18,.28);

/* Postal abierta */
--shadow-paper-deep:
  0 1px 1px rgba(26,22,18,.04),
  0 2px 4px rgba(26,22,18,.06),
  0 8px 16px rgba(26,22,18,.10),
  0 24px 48px -8px rgba(26,22,18,.18),
  inset 0 0 80px rgba(184,137,62,.10);

/* Sello bermellón elevado */
--shadow-seal:
  0 2px 4px rgba(200,56,42,.25),
  0 8px 16px rgba(200,56,42,.30),
  0 16px 32px -4px rgba(200,56,42,.40);

/* Sello dorado luminoso */
--shadow-gold-glow:
  0 0 0 1px rgba(184,137,62,.30),
  0 0 24px rgba(255,216,158,.40),
  0 8px 16px rgba(184,137,62,.35);
```

---

## 3 · Sistema de animación maestro

### 3.1 Curvas de movimiento (estandarizar)

```css
:root {
  --ease-paper:   cubic-bezier(0.16, 1, 0.3, 1);     /* abrir papel (existente) */
  --ease-soft:    cubic-bezier(0.4, 0, 0.2, 1);       /* UI neutra (existente) */
  --ease-brush:   cubic-bezier(0.65, 0, 0.35, 1);     /* pincelada kanji */
  --ease-sakura:  cubic-bezier(0.34, 1.56, 0.64, 1);  /* pétalo cayendo */
  --ease-photo:   cubic-bezier(0.87, 0, 0.13, 1);      /* revelado foto */
  --ease-seal:    cubic-bezier(0.34, 1.56, 0.64, 1);  /* golpe de sello */
}
```

### 3.2 Tiempos (estandarizar)

| Categoría | Duración | Curva |
|---|---|---|
| Micro-interacción (hover, focus) | 180–250 ms | `--ease-soft` |
| Cambio de estado (entrar/salir) | 400–600 ms | `--ease-paper` |
| Revelado foto polaroid | 1100–1400 ms | `--ease-photo` |
| Pincelada kanji | 1400–1800 ms | `--ease-brush` |
| Pétalo cayendo | 6000–14000 ms | `--ease-sakura` |
| Sello estampándose | 320 ms | `--ease-seal` |
| Línea trazándose mapa | 1500–2200 ms | `--ease-paper` |
| Transición postal→primera pregunta | 1200 ms | `--ease-paper` |

### 3.3 Sistema de partículas de pétalos de sakura

**Componente nuevo: `SakuraField`** — canvas fixed positioned detrás de todo.

```js
class SakuraField {
  constructor(opts = {}) {
    this.count = opts.count ?? 26;          // 18–32 desktop, 12–18 mobile
    this.windBase = opts.windBase ?? 0.3;
    this.canvas = document.createElement('canvas');
    this.ctx = this.canvas.getContext('2d');
    // listeners, resize, raf
  }
  spawn() {
    return {
      x: Math.random() * this.w,
      y: -20 - Math.random() * 200,
      size: 6 + Math.random() * 10,
      rot: Math.random() * Math.PI * 2,
      rotSpeed: (Math.random() - 0.5) * 0.012,
      vx: 0.2 + Math.random() * 0.4,
      vy: 0.3 + Math.random() * 0.6,
      wobblePhase: Math.random() * Math.PI * 2,
      wobbleAmp: 0.8 + Math.random() * 1.2,
      wobbleFreq: 0.005 + Math.random() * 0.01,
      opacity: 0.5 + Math.random() * 0.4,
      hue: Math.random() < 0.7 ? 'sakura' : 'sakura-pale',
      life: 0
    };
  }
  tick(p) {
    p.life++;
    p.x += p.vx + Math.sin(p.life * p.wobbleFreq + p.wobblePhase) * p.wobbleAmp * 0.6;
    p.y += p.vy;
    p.rot += p.rotSpeed;
    // dibujar SVG-like con paths simplificados
  }
}
```

**Detalles críticos**:
- ❗ **No bloom ni glow**: pétalos son formas planas con sombra CSS simulada (canvas: `shadowBlur: 4, shadowColor: rgba(216,160,168,0.4)`).
- ❗ **Respetar `prefers-reduced-motion`**: reducir `count` a 4 y bajar velocidades 50%.
- ❗ **Mobile**: `count = 14`, `dpr = Math.min(window.devicePixelRatio, 2)`.
- ❗ **Throttle de FPS**: si `requestAnimationFrame` reporta `>22ms` por frame, reducir `count`.
- ❗ **Z-index**: por debajo del contenido interactivo, por encima del fondo.

**Dibujo del pétalo** (en canvas, no sprite):
```js
// pétalo de 5 pétalos más pequeños alrededor
ctx.save();
ctx.translate(p.x, p.y);
ctx.rotate(p.rot);
ctx.fillStyle = p.hue === 'sakura' ? '#F2C7C7' : '#FFE4E8';
ctx.beginPath();
ctx.ellipse(0, 0, p.size, p.size * 0.55, 0, 0, Math.PI * 2);
ctx.fill();
ctx.fillStyle = 'rgba(216,160,168,0.5)';
ctx.beginPath();
ctx.arc(0, 0, p.size * 0.15, 0, Math.PI * 2);
ctx.fill();
ctx.restore();
```

### 3.4 Sistema de kanji pincelada

**Componente: `KanjiBrush`** — pinta un kanji con stroke-by-stroke reveal.

**Estrategia**: en lugar de animar el path completo (técnicamente posible pero menos impactante), usamos **una secuencia de capas SVG** donde cada trazo se destapa con `clip-path` animado.

```html
<svg viewBox="0 0 200 200" class="kanji-brush">
  <defs>
    <clipPath id="stroke1"><path d="..."/></clipPath>
    <clipPath id="stroke2"><path d="..."/></clipPath>
    <!-- ... -->
  </defs>
  <g class="kanji-brush__ink" filter="url(#inkRoughen)">
    <path class="stroke" data-stroke="1" d="..."/> <!-- trazo 1 -->
    <path class="stroke" data-stroke="2" d="..."/> <!-- trazo 2 -->
    <!-- ... -->
  </g>
</svg>
```

```css
.kanji-brush__ink .stroke {
  /* cada trazo se anima con clip-path que se expande */
  /* simula la velocidad variable del pincel (presión) */
}
```

**Kanji que aparecerán (uno por momento clave)**:

| Momento | Kanji | Significado | Aparece |
|---|---|---|---|
| Sello postal | `旅` | viaje | estático (ya está) |
| Estado postal | `待` | esperar | aparece al hacer hover al CTA |
| Inicio Q1 | `始` | comenzar | pincelada al elegir 1ª opción |
| Transición Tokio→Intermedio | `道` | camino | pincelada completa durante la transición |
| Transición Intermedio→Kioto | `美` | belleza | pincelada completa |
| Transición Kioto→Onsen | `湯` | agua caliente | pincelada completa |
| Antes del mapa final | `約束` | promesa | dos kanji pincelada secuencial |
| Despedida | `縁` | destino/afinidad | pincelada lenta, definitiva |

**Cómo construir los paths**: cada kanji se vectoriza en SVG con orden de trazos (idealmente desde una fuente SVG real, p.ej. KanjiVG). Mantener una librería `kanji/` con cada uno como SVG con `<g class="stroke-N">`.

### 3.5 Sistema de revelado de fotos (polaroid real)

**Componente: `PhotoReveal`** — cuando un acto aparece, la foto pasa por 4 fases:

1. **0–180ms**: aparece un marco polaroid blanco sin foto.
2. **180–900ms**: la imagen se "revela" con un wipe horizontal (efecto albúmina antigua).
3. **900–1100ms**: pequeño latido de escala (`1 → 1.02 → 1`).
4. **1100ms+**: hover disponible, ligero tilt 3D basado en mouse.

```css
.act__photo {
  position: relative;
  clip-path: inset(0 100% 0 0); /* empieza invisible desde la derecha */
  animation: photoReveal 900ms var(--ease-photo) forwards;
  transition: transform 400ms var(--ease-paper);
}
@keyframes photoReveal {
  0%   { clip-path: inset(0 100% 0 0); filter: brightness(1.3) contrast(0.9); }
  60%  { clip-path: inset(0 0 0 0); filter: brightness(1.15) contrast(0.95); }
  100% { clip-path: inset(0 0 0 0); filter: brightness(1) contrast(1); }
}
```

**Tilt 3D en hover**:
```js
// Solo en (hover: hover) and (pointer: fine). En móvil, tilt automático al entrar.
const finePointer = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
if (finePointer) {
  photoEl.addEventListener('mousemove', (e) => {
    const r = photoEl.getBoundingClientRect();
    const cx = (e.clientX - r.left) / r.width - 0.5;
    const cy = (e.clientY - r.top) / r.height - 0.5;
    photoEl.style.transform = `perspective(900px) rotateY(${cx * 8}deg) rotateX(${-cy * 8}deg) scale(1.04)`;
  });
  photoEl.addEventListener('mouseleave', () => {
    photoEl.style.transform = '';
  });
} else {
  // En touch: tilt automático que oscila (efecto papel meciéndose)
  photoEl.style.animation = 'photoSway 4.5s var(--ease-paper) 1.4s 1';
}
```

### 3.6 Cursor personalizado — DESCARTADO

En mobile-first **no hay cursor personalizado**. El navegador muestra el cursor nativo del sistema cuando aplica (escritorio) y nada en táctil. Toda la inversión se va a **inmersión automática**: animaciones auto-play al cargar cada estado, sin esperar gesto.

---

## 4 · Transformación estado por estado

### 4.1 ESTADO 0 — La postal (ahora más inmersiva)

**Antes**: postal estática con sello, título y botón.

**Después**: **cinemática de apertura de carta**. Flujo:

1. **0–0ms** (al cargar): pantalla casi negra, ligera textura de papel visible (`opacity: 0.05`).
2. **200–600ms**: aparece un sobre cerrado centrado, kanji `便` (郵便 correo) escrito muy tenue en él.
3. **600–900ms**: el sobre se desliza hacia arriba y se abre — flap superior rota 180°.
4. **900–1100ms**: la postal sale del sobre con un sutil ease-out, deja ver un borde de papel envejecido.
5. **1100–1600ms**: el sello bermellón `旅` se estampa con animación de presión (escala 1.4 → 0.95 → 1, con un halo bermellón expandiéndose).
6. **1600–2200ms**: el nombre "Noelia," aparece con la manuscrita, letter-by-letter usando `--ease-brush`.
7. **2200–2900ms**: el título "Crónica de un viaje anunciado" se pinta línea por línea.
8. **2900–3200ms**: el cuerpo del texto aparece con fade.
9. **3200ms+**: el CTA "comienza el viaje" se ilumina, y debajo aparece un micro-texto: "toca o pulsa enter — la carta te espera".

**Detalles extra**:
- Sonido opcional: un sutil `paper unfold` al abrir (Web Audio API, no archivo, sintetizado — 100ms de ruido blanco con filtro pasa-bajos).
- `prefers-reduced-motion`: salta directamente a postal ya revelada en 0ms.

**Componente a introducir**: `EnvelopeIntro` (sólo aparece en sesión nueva desde el inicio).

### 4.2 ESTADO 1–7 — Preguntas (preguntas que respiran)

**Mejoras transversales**:
- **Fondo vivo**: capa `SakuraField` siempre presente (configurable por estado).
- **Mapa de fondo** ya existe — mejorarlo:
  - Cambiar el viewBox para que **rote muy ligeramente** (2–3 grados) en idle, simulando papel sobre una mesa.
  - El nodo activo debe tener **un halo dorado** animado (no sólo el pulso actual).
- **Opciones**:
  - Hover: la opción se levanta 4px y proyecta sombra dorada.
  - Click: micro-stamp effect (halo bermellón).
  - Cada opción tiene un **micro-icono SVG distinto** (no emoji): un gato (Yanesen), un dragón (Akihabara), un buda (Templo), etc.

**Momento único por pregunta** (uno de los 7):

| Q | Momento WOW |
|---|---|
| Q1 | El kanji `始` se pincelada en grande en el fondo mientras se carga el acto. |
| Q4 (intermedio) | Las opciones muestran un mini-mapa interactivo del destino — Magome→Tsumago animado, Alpes con niebla moviéndose, Shinkansen cruzando. |
| Q6 (Kōya-san) | Al elegir Kōya-san, las opciones se oscurecen brevemente y aparecen 200.000 lucecitas en el fondo (representando los faroles de Okunoin) — son partículas naranjas/doradas que parpadean, no reales (sería 1 bombilla = 1 DOM node, imposible), sino **canvas con 80 partículas naranjas**. |
| Q7 (onsen) | Al elegir onsen, aparece una capa de vapor sutil en la parte inferior de la pantalla (canvas con ondulaciones suaves). |

### 4.3 ESTADO "thought" (el pensamiento antes de los actos)

**Antes**: una pantalla con texto rojo y un punto "toca para continuar".

**Después**:
- El texto del `micro` aparece **pincelada por pincelada** con la `Caveat` o manuscrita mejorada.
- Debajo, **aparece lentamente un kanji** que resume el pensamiento:
  - Para "calm": `静` (calma).
  - Para "neon": `夜` (noche).
  - Para "market": `味` (sabor).
- El "toca para continuar" se desvanece después de 3 segundos, dejando sólo el kanji.
- Al tocar, los pétalos de sakura se intensifican brevemente (count x3) y vuelven a la normalidad.

### 4.4 ESTADO "transition" (entre nodos) — el momento WOW por excelencia

**Antes**: mapa a pantalla completa con línea dibujándose.

**Después**: **escena cinematográfica en 3 actos**:

1. **Acto A (0–800ms)**: el estado actual hace `fade-out` mientras una cortina de papel (panel beige) baja desde arriba y sube desde abajo, encontrándose en el centro.
2. **Acto B (800–2800ms)**: el mapa a pantalla completa aparece. Pero ahora:
   - El kanji de transición (`道`, `美`, `湯`) se pincelada **en grande** (60% de la pantalla) **antes** de que el mapa aparezca.
   - El mapa aparece debajo con `clip-path` que se abre desde el kanji hacia afuera (efecto "el kanji perfora la realidad").
   - La línea entre nodos se dibuja con un **pincel con partícula al frente** (un círculo bermellón que viaja por la línea a la vez que se traza).
   - Los labels "de Tokio a Nakasendō" aparecen como sobrescritos a mano por encima.
3. **Acto C (2800–3500ms)**: el mapa se encoge hacia su destino final, dejando paso a la siguiente pregunta.

**Cambio técnico**: en lugar de `position: fixed` y opacidad, usar **`View Transitions API`** (Chrome 111+) con fallback a fade para Safari/Firefox.

### 4.5 ESTADO "mapa" — el pergamino cobra vida

**Mejoras**:
- **El pergamino tiene textura física**: un SVG `feTurbulence` aplicado a `feDisplacementMap` genera una superficie irregular que se anima al mover el mouse (efecto "tactile paper").
- **Los nodos activos** laten con un halo dorado. Los no activos: opacity 0.4 con un gris tenue.
- **Conexiones activas**: la línea se traza de nuevo cada vez que se entra al estado, en orden (primero Tokio, luego la siguiente, etc.).
- **Polaroids**: ahora se revelan uno a uno (cada 180ms) con `PhotoReveal`, no con scale simple.
- **Hover sobre polaroid**: la polaroid se levanta, se inclina 3D hacia el mouse, proyecta sombra dorada y muestra un tooltip con el nombre del lugar en japonés + romaji.

### 4.6 ESTADO "despedida" — el clímax emocional

**Antes**: bloques de texto que aparecen secuencialmente con fade.

**Después** — **experiencia de cierre completa**:

1. **0–600ms**: pantalla en negro pergamino. Aparece el sello `A · N` con su estampa dorada.
2. **600–1200ms**: el kanji `縁` (destino/afinidad) se pincelada muy lentamente en grande, en oro, en el centro.
3. **1200–2400ms**: el kanji se desvanece y aparece el texto de la despedida, pero ahora escrito **como si fuera a mano**: cada letra de "Primero fue Tailandia, en nuestra luna de miel..." se pinta con una animación de stroke (usando SVG `<text>` con `stroke-dasharray`).
4. **2400–3200ms**: los pétalos de sakura se intensifican (count x3).
5. **3200–4500ms**: aparece la firma manuscrita "te quiero" (Caveat, más cálida que Great Vibes), con un pequeño trazo que la cruza como si fuera firmada.
6. **4500ms+**: el sello final `A · N` se estampa por segunda vez, más pequeño, en una esquina.
7. **5000ms+**: un botón ghost "volver al inicio" con cursor pointer.

**Detalle WOW**: al final, durante 5 segundos, los pétalos caen en cascada vertical completa antes de detenerse y quedarse en el campo normal.

---

## 5 · Micro-detalles WOW (los que marcan la diferencia x100)

### 5.1 Textura de papel mejorada

La textura actual (`feTurbulence` muy sutil) se queda corta. Reemplazar por:

```css
body::before {
  content: '';
  position: fixed; inset: 0; pointer-events: none; z-index: -1;
  background:
    /* ruido fino */
    url("data:image/svg+xml,...feTurbulence baseFrequency=0.85..."),
    /* fibras de papel largas */
    url("data:image/svg+xml,...feTurbulence baseFrequency=0.04 numOctaves=2..."),
    /* manchas sutiles */
    radial-gradient(circle at 20% 30%, rgba(184,137,62,0.05) 0%, transparent 40%),
    radial-gradient(circle at 80% 70%, rgba(26,22,18,0.04) 0%, transparent 50%);
  mix-blend-mode: multiply;
  opacity: 0.6;
}
```

### 5.2 Sellos bermellón con textura real

El sello actual es un SVG plano. Mejorarlo:

```svg
<filter id="inkStamp">
  <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="3"/>
  <feDisplacementMap in="SourceGraphic" scale="2"/>
  <feColorMatrix values="0 0 0 0 0.78
                          0 0 0 0 0.22
                          0 0 0 0 0.16
                          0 0 0 0.92 0"/>
</filter>
```

Esto le da al sello una **textura irregular**, como tinta real que no cubrió perfectamente el papel.

### 5.3 Hover en opciones — la que se eleva

```css
.q__option {
  transition:
    transform 200ms var(--ease-paper),
    border-color 200ms ease,
    background 200ms ease,
    box-shadow 300ms var(--ease-paper);
}
.q__option:hover {
  transform: translateY(-2px);
  border-color: var(--gold);
  box-shadow: 0 4px 12px rgba(184,137,62,0.15), 0 0 0 1px rgba(184,137,62,0.1);
}
```

### 5.4 Botones con shimmer

```css
.btn {
  position: relative;
  overflow: hidden;
}
.btn::after {
  content: '';
  position: absolute; inset: 0;
  background: linear-gradient(105deg,
    transparent 30%,
    rgba(255,255,255,0.3) 50%,
    transparent 70%);
  transform: translateX(-100%);
  transition: transform 600ms var(--ease-paper);
}
.btn:hover::after { transform: translateX(100%); }
```

### 5.5 Scroll suave entre estados

Aprovechar **CSS Scroll Snap** o **View Transitions API** (lo que esté disponible):

```css
@media (prefers-reduced-motion: no-preference) {
  .state {
    transition: opacity 800ms var(--ease-paper),
                transform 800ms var(--ease-paper);
  }
  .state[data-active="false"] {
    opacity: 0;
    transform: translateY(20px) scale(0.99);
  }
}
```

### 5.6 Hint tipográfico en los momentos justos

- Después de cada opción elegida, una frase en `Cormorant Infant Italic` aparece: "perfecto" o "sí, esto me gusta" durante 800ms.
- Antes de la despedida: "una cosa más" en la manuscrita.

### 5.7 Efecto "papel levantado" al hacer hover en topbar

```css
.topbar {
  background: linear-gradient(180deg,
    rgba(244,236,224,0.92) 0%,
    rgba(244,236,224,0.85) 100%);
  box-shadow:
    inset 0 -1px 0 rgba(184,137,62,0.2),
    0 4px 12px rgba(26,22,18,0.05);
}
```

### 5.8 Marca de agua sutil: tu firma

En cada página, **en la esquina inferior derecha**, aparece un micro sello `A · N` (15px) con opacity 0.15. Sólo se ve si miras. Es tu firma invisible.

---

## 6 · Refinamiento por sección (detalles finos)

### 6.1 Topbar
- Logo "旅 · Japón, pronto" pero ahora con micro-animación: el `旅` rota 360° lentamente (30s loop) en idle.
- Botón "volver al inicio": hover muestra tooltip "relee la carta" en manuscrita.

### 6.2 Botón principal (CTA)
- El CTA "comienza el viaje" debe tener un **breathing animation** cuando está idle (sube 2px y baja, cada 2.4s).
- El hover state debe tener sombra dorada más marcada y micro-stamp effect.

### 6.3 Polaroid en actos
- La polaroid debe tener **un pequeño handwritten caption** en la zona inferior, no tipográfica — algo como una nota a mano.

### 6.4 Mapa pergamino
- Animación inicial al entrar al estado mapa: el pergamino se "desenrolla" desde el centro (clip-path horizontal que se expande).

---

## 7 · Performance y accesibilidad

### 7.1 Performance
- **Pétalos**: usar canvas, no DOM (cada pétalo como elemento DOM sería mortal).
- **Kanji SVG**: pre-renderizar y cachear las trayectorias (no recalcular en cada frame).
- **Imágenes**: convertir todas las `.jpg/.webp/.png` actuales a **AVIF + WebP fallback** + `loading="lazy"`.
- **Fuentes**: `font-display: swap` en todas + subset de kanji (sólo los caracteres que aparecen: `旅 待 始 道 美 湯 約束 縁 便 郵便 静 夜 味`).
- **Code splitting**: cargar el `SakuraField` sólo después de que la postal se abra, no al inicio.

### 7.2 Accesibilidad
- ❗ **Mantener todo el soporte `prefers-reduced-motion`** existente y expandirlo:
  - Sin partículas.
  - Sin kanji animado (aparece de golpe).
  - Sin transiciones de opacidad largas (instantáneo).
  - Sin breathing animation.
- ❗ **Focus visible**: oro en lugar de negro para mejor contraste en papel.
- ❗ **Lectura de pantalla**: añadir `aria-live="polite"` en el cambio de estado.
- ❗ **Reduced motion + particles**: ni se carga el canvas.

### 7.3 Responsive
- Móvil (320–520px): polaroids más pequeñas, kanji más pequeño, partículas a la mitad.
- Tablet (768–1024px): todo normal.
- Desktop (1440px+): detalle máximo, partículas al máximo.

---

## 8 · Plan de implementación por fases

> **Estrategia**: hacer **un cambio a la vez, midiendo impacto**. El estado actual ya es bueno, así que no rehacer, sino **sobre-poner**.

### Fase 0 — Cimientos (1 sesión)
- [ ] Refinar paleta y tokens en `:root` (sin tocar componentes).
- [ ] Añadir nuevas fuentes a `<head>` con `font-display: swap`.
- [ ] Añadir subset de kanji como variable CSS.
- [ ] **No tocar nada visual todavía.**

### Fase 1 — Atmósfera (1 sesión)
- [ ] Crear `SakuraField` (canvas con 26 partículas).
- [ ] Integrarlo detrás de todo, desactivable con `prefers-reduced-motion`.
- [ ] Ajustar densidad por viewport.
- [ ] **QA visual**: ¿se ve atmósfera sin distraer?

### Fase 2 — Cinemática de apertura (1 sesión)
- [ ] Reescribir el estado `s-postal` para que sea la escena del sobre abriéndose.
- [ ] Implementar sello estampándose con `filter` ink-stamp.
- [ ] Letter-by-letter del nombre "Noelia,".
- [ ] **QA emocional**: ¿te dan ganas de seguir leyendo?

### Fase 3 — Sistema kanji (1.5 sesiones)
- [ ] Crear `KanjiBrush` componente.
- [ ] Vectorizar los 8 kanji necesarios (idealmente usar KanjiVG).
- [ ] Integrar en transiciones entre nodos.
- [ ] **QA narrativo**: ¿los kanji ayudan o distraen?

### Fase 4 — Polaroids y fotos (1 sesión)
- [ ] Reescribir `.act__photo` con `PhotoReveal`.
- [ ] Tilt 3D en hover.
- [ ] Animar scrapbook del mapa con reveal escalonado.
- [ ] **QA háptico**: ¿se siente físico?

### Fase 5 — Transiciones y despedida (1.5 sesiones)
- [ ] Reescribir `s-transition` con cortina de papel + kanji + pincel.
- [ ] Reescribir `s-despedida` con pincelada `縁` + firma manuscrita.
- [ ] **QA emocional**: ¿es el cierre que mereces?

### Fase 6 — Detalles finos (1 sesión)
- [ ] Cursor personalizado.
- [ ] Shimmer en botones.
- [ ] Breathing en CTA principal.
- [ ] Marca de agua sutil `A · N`.
- [ ] Hover con elevación en opciones.
- [ ] Topbar con rotación lenta del kanji.

### Fase 7 — Polish y QA (1 sesión)
- [ ] Lighthouse mobile (perf + a11y + best practices).
- [ ] Verificar prefers-reduced-motion en cada estado.
- [ ] Cross-browser (Chrome, Safari, Firefox, Samsung Internet).
- [ ] Cross-device (iPhone SE, Pixel 7, iPad, MacBook).
- [ ] Optimización de imágenes (AVIF + WebP).
- [ ] **QA final**: ¿te pone la piel de gallina al enseñárselo a Noelia?

---

## 9 · Riesgos y decisiones pendientes

| Riesgo | Mitigación |
|---|---|
| Demasiadas partículas = distrae | Fase 1 con count=14, subir a 26 sólo si usuario lo aprueba |
| Kanji mal vectorizados = parecen "tipeados", no pintados | Usar KanjiVG (público, gratuito) y validar visualmente |
| Cinemática de apertura muy larga (3s) = usuarios impacientes | Botón "saltar intro" visible desde el inicio |
| Tilt 3D = mareo en algunos usuarios | Cap a 6 grados de rotación max, desactivar en `prefers-reduced-motion` |
| Pincel de kanji = muy lento en Safari | Hacer fallback a fade-in para Safari < 17 |
| Performance en móviles gama baja | Throttle partículas automáticamente si FPS < 50 |

---

## 10 · Métricas de éxito

**Antes** (estado actual):
- Engagement: alto (ya es bonito).
- Tiempo en página: medio.
- Wow factor: 6/10.

**Después** (target):
- Engagement: muy alto.
- Tiempo en página: +80% (gente pausando para mirar los pétalos, los kanji).
- Wow factor: 10/10 — "esto no se parece a nada que haya visto en una web".
- Emocional: que Noelia llore, que Adrián se sienta orgulloso de haberlo construido.

---

## 11 · Decisiones confirmadas (cierre de fase de planificación)

| Decisión | Resolución |
|---|---|
| **Apertura** | Sobre abriéndose → postal sale → sello se estampa → texto letra a letra (cinemática completa) |
| **Pétalos sakura** | Sólo en momentos clave: transiciones entre nodos, reveal de polaroids en scrapbook, despedida. NO constante. |
| **Cursor personalizado** | Descartado. Prioridad absoluta: **mobile-first**. Touch devices no necesitan cursor. |
| **Inicio implementación** | Fase 0 + Fase 1 combinadas: cimientos + sakura puntual. |

### Implicaciones técnicas de las decisiones

**Mobile-first obligatorio**:
- NO habrá `:hover`-only reveals. Todo debe funcionar con `tap` + `:focus-visible` + scroll.
- NO habrá cursor personalizado (ya descartado).
- NO habrá tilt 3D que requiera mouse (sólo en `@media (hover: hover) and (pointer: fine)`).
- Touch targets mínimo 44x44px (ya está en `.q__option { min-height: 48px }`).
- Gestos: `swipe` opcional para navegar entre actos (con `prefers-reduced-motion` desactivado).
- Pétalos en canvas con `count = max(8, Math.min(window.innerWidth / 50, 18))`.

**Sakura en momentos clave (no permanente)** — lista de disparadores:

| Disparador | Tipo | Intensidad | Duración |
|---|---|---|---|
| Inicio apertura postal | burst | 40 | 4s |
| Pincelada de kanji en transición | continuous | 24 | hasta fin de transición |
| Reveal de cada polaroid en scrapbook | burst | 18 | 1.5s |
| Pensamiento (thought) | continuous | 14 | hasta tap |
| Despedida final | cascade | 60 | 8s |

**Implementación**: API `SakuraField.burst(opts)` y `SakuraField.stream(opts)` en lugar de loop continuo.