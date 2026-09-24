export const meta = {
  name: 'canal-sur-especifico',
  description: 'Temario específico de un puesto de Canal Sur: investigar por bloques, redactar reutilizando RTVE y el común, verificar, refutar, rematar y esquema',
  phases: [
    { title: 'Investigar', detail: 'un agente por bloque de temas que comparten fuentes' },
    { title: 'Tema', detail: 'copiar o redactar → verificar → refutar → rematar → esquema' },
  ],
}
// args: {puesto, slug, nombre, temas: {n: {rtve?, repite?}}, bloques: [{id, temas, nota}], comun: {n: [ficheros]}}

let libres = 3; const cola = []
const turno = () => libres > 0 ? (libres--, Promise.resolve()) : new Promise(r => cola.push(r))
const suelta = () => { const r = cola.shift(); r ? r() : libres++ }
const A = async (p, o) => { await turno(); try { return await agent(p, o) } finally { suelta() } }

const { puesto: P, slug: S, nombre: N } = args
const TD = `temas/canal-sur-especificos/${S}`, ED = `esquemas/canal-sur-especificos/${S}`, INF = `informes/canal-sur-especificos/${P}`
const BASE = `Temario específico de ${N} de Canal Sur (puesto ${P}). Lee SOLO informes/canal-sur-especificos/ENCARGO.md (no abras metodo/) y el enunciado convocatoria/canal-sur/especificos/${S}.md. Hoy es 24-09-2026. Temas en ${TD}/NN-<slug>.md; informes ${INF}-*.md. Respuesta final: 120 palabras como máximo.`
const nn = n => String(n).padStart(2, '0')
const REFUTA = { type: 'object', properties: { graves: { type: 'integer' }, menores: { type: 'integer' }, lagunas: { type: 'integer' } }, required: ['graves', 'menores', 'lagunas'] }
const REMATE = { type: 'object', properties: { amplio: { type: 'boolean' } }, required: ['amplio'] }

const reuso = n => {
  const t = args.temas[String(n)] || {}, c = (args.comun || {})[String(n)] || []
  let s = ''
  if (c.length) s += `\nYA CERRADO Y VERIFICADO (común de Canal Sur o puesto anterior, redacción vigente): ${c.join(', ')}. Copia literal los pasajes que sirvan; no los reescribas.`
  if (t.rtve) s += `\nDE RTVE (${t.rtve.pct} % del enunciado; ${t.rtve.nota}): ${t.rtve.ficheros.join(', ')}. Copia literal lo que valga${t.rtve.actualizar === 'sí' ? ', releyendo cada precepto en su redacción vigente' : ''} y quita lo propio de RTVE.`
  return s
}

const tema = async (n, bloque) => {
  const T = nn(n), lb = x => `T${T} ${x}`, ph = 'Tema', F = `${TD}/${T}-*.md`
  const rep = (args.temas[String(n)] || {}).repite
  if (rep && rep.tipo === 'identico') {
    await A(`${BASE}\nEl tema ${n} es idéntico al tema ${rep.tema} del puesto ${rep.puesto} (temas/canal-sur-especificos/${rep.puesto}-*/${nn(rep.tema)}-*.md). Cópialo a ${TD}/${T}-<mismo slug>.md cambiando SOLO el título y la ficha a este puesto y número; copia igual su esquema a ${ED}/. Si el original no existe aún, dilo y no hagas nada.`, { label: lb('copiar'), phase: ph, model: 'haiku' })
    return T
  }
  const base = rep ? `\nEl tema es parecido al tema ${rep.tema} del puesto ${rep.puesto} (temas/canal-sur-especificos/${rep.puesto}-*/${nn(rep.tema)}-*.md): parte de su texto y amplía SOLO lo que este enunciado pida de más.` : ''
  await A(`${BASE}\nFASE 2 · REDACTAR el tema ${n}. Material: ${INF}-investigacion-${bloque.id}.md.${base}${reuso(n)}\nEscribe por partes guardando cada epígrafe. En el informe ${INF}-T${T}-redaccion.md, lista bajo «Copiado del común» los epígrafes copiados literal de temas ya cerrados de Canal Sur, y bajo «Copiado de RTVE sin cambios» los pasajes técnicos copiados literal, sin tocar una palabra, de temas de RTVE marcados sin actualizar.\nANTES DE ENTREGAR: escribe 10 preguntas tipo test que un tribunal haría sobre este enunciado (repartidas por todas sus rúbricas, teoría y aplicación práctica) y comprueba que el tema las contesta enteras; si no, amplía el tema. Ponlas al final del informe de redacción.`, { label: lb('redactar'), phase: ph })
  await A(`${BASE}\nFASE 3 · VERIFICAR ${F}. Relee cada dato en su fuente con los nueve errores delante; corrige y quita lo que no confirmes. NO re-verifiques los pasajes listados bajo «Copiado del común» ni bajo «Copiado de RTVE sin cambios» en ${INF}-T${T}-redaccion.md (ya pasaron el ciclo completo); comprueba solo con diff o grep que son literales. Sí verifica todo lo demás, incluido lo de RTVE que se haya adaptado o que cite normas. Lentes que tocan (ENCARGO). Informe ${INF}-T${T}-verificacion.md.`, { label: lb('verificar'), phase: ph })
  const r = await A(`${BASE}\nFASE 4 · REFUTAR (no corriges) ${F}: exactitud contra la fuente (salvo lo «Copiado del común» y lo «Copiado de RTVE sin cambios», ver ${INF}-T${T}-redaccion.md; la cobertura sí mira el tema entero) y cobertura del enunciado. 15 preguntas tipo test de 4 opciones (teoría y aplicación práctica) en ${INF}-T${T}-preguntas.md, contestadas solo con el tema: entera / a medias / no. Informe ${INF}-T${T}-refutacion.md.`, { label: lb('refutar'), phase: ph, schema: REFUTA })
  if (r && r.graves + r.menores + r.lagunas > 0) {
    const m = await A(`${BASE}\nFASE 5 · REMATAR ${F} con ${INF}-T${T}-refutacion.md y -preguntas.md. Comprueba cada corrección en la fuente antes de aplicarla. Laguna: se amplía el tema, nunca se recorta la pregunta. Corre indice.py y las lentes que tocan. Informe ${INF}-T${T}-remate.md con los pasajes cambiados. Devuelve si ampliaste contenido nuevo.`, { label: lb('rematar'), phase: ph, schema: REMATE, model: r.lagunas > 0 ? undefined : 'sonnet' })
    if (m && m.amplio) await A(`${BASE}\nFASE 5 bis · Revisa SOLO los pasajes que cambió el remate de ${F} (lista en ${INF}-T${T}-remate.md): cada dato contra su fuente y su antecedente; corrige comprobando en la fuente. Informe ${INF}-T${T}-final.md.`, { label: lb('final'), phase: ph })
  }
  await A(`${BASE}\nESQUEMA de ${F} en ${ED}/ con el mismo nombre, SIN abrir otros esquemas: formato = título «# Tema N del específico de <Puesto> · <título>», línea **Siglas**, una línea «Esqueleto para repasar, no resumen…», <!-- indice --><!-- /indice -->, y un ## por rúbrica del enunciado con líneas telegráficas, la fuente o el precepto delante de cada una. ≤2.000 palabras / 130 líneas; se quita explicación, nunca un dato; nada que no esté en el tema. Lee el tema una sola vez.`, { label: lb('esquema'), phase: ph, model: 'sonnet' })
  return T
}

return await pipeline(args.bloques,
  b => A(`${BASE}\nFASE 1 · INVESTIGAR el bloque ${b.id}: temas ${b.temas.join(', ')}. ${b.nota}\nLo reutilizable ya está localizado (RTVE y común) y lo leerá el redactor: tú investiga SOLO lo que falta para cubrir el enunciado.${b.temas.map(n => reuso(n) ? `\nTema ${n}:${reuso(n)}` : '').join('')}\nMaterial denso con la fuente y la cita literal pegadas a cada dato, por tema y epígrafe, y lo que no pudiste confirmar. Escríbelo según avances en ${INF}-investigacion-${b.id}.md. SI ESE FICHERO YA EXISTE, léelo, compléta solo lo que falte y no repitas lo hecho.`, { label: `investigar ${b.id}`, phase: 'Investigar' }),
  (_, b) => parallel(b.temas.map(n => () => tema(n, b)))
)
