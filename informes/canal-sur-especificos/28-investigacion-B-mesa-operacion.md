# Investigación · Operador/a de Sonido (28) · bloque B-mesa-operacion (temas 4, 6, 7, 8, 9)

Fase 1. Fecha de trabajo y de lectura de todas las fuentes: **25-09-2026** (salvo que se diga otra).
Sólo lo que falta sobre lo reutilizable de RTVE (ing-sup-teleco/12, tese/10, ing-tec-teleco/12,
realizacion-tv/17 y 18, sonido/06, 08, 09 y 12, informacion-grafica/06, realizacion/09, produccion/11).
Cita literal entre comillas; en inglés tal cual la fuente. Lo que no se pudo confirmar va al final.
No se ha encontrado ningún documento publicado de RTVA/CSRTV sobre equipamiento u operación de
sonido: todo lo propio de CSRTV queda para «Lo que este tema no da».

## Fuentes leídas (25-09-2026)

- EBU Tech 3326, *Audio contribution over IP – Requirements for Interoperability*, Tech. Spec. Rev. 4, Ginebra, noviembre 2014. https://tech.ebu.ch/docs/tech/tech3326.pdf
- EBU Tech 3368, *Audio contribution over IP – Profiles*, versión 1.0, Ginebra, noviembre 2014. https://tech.ebu.ch/docs/tech/tech3368.pdf
- Yamaha Corporation, *CL5/CL3/CL1 V5 Reference Manual* (manual de fabricante de una consola digital de directo). https://usa.yamaha.com/files/download/other_assets/3/1205593/cl5_3_1_en_rm_f0.pdf
- Soundcraft (Harman International), *The Soundcraft Guide to Mixing*, ref. ZL0439, ed. 08/01 (2001). Copia en https://music.arts.uci.edu/dobrian/w14/music151/thesoundcraftguidetomixing.pdf (web de la Universidad de California en Irvine).
- Yamaha Corporation of America, Doug Gould, *Get on the Bus. How to Route Input Signals* (guía divulgativa del fabricante, sin fecha). https://yamaha.com/US/houseofworship/downloadables/Audio-System-How-to-Guides/How-to-Route-Input-Signals-Guide.pdf
- Avid Technology, *Pro Tools Reference Guide*, versión 2025.12, cap. 55 «Automation». https://resources.avid.com/SupportFiles/PT/Pro_Tools_Reference_Guide_2025.12.pdf
- EBU R 68-2000, *Alignment level in digital audio production equipment and in digital audio recorders* (primera ed. 1992, rev. 1995-2000). https://tech.ebu.ch/docs/r/r068.pdf
- AES, *Technical Document AESTD1008.1.21-9 (supersedes TD1004). Recommendations for Loudness of Internet Audio Streaming and On-Demand Distribution*, 24-09-2021. https://aes.org/wp-content/uploads/2024/01/20210924_TD1008_v3.13.pdf
- IETF RFC 8216, R. Pantos y W. May, *HTTP Live Streaming*, agosto 2017 (Informational). https://www.rfc-editor.org/rfc/rfc8216.txt
- Apple, *Audio requirements – Apple Podcasts for Creators* (página web sin fecha visible). https://podcasters.apple.com/support/893-audio-requirements
- EBU Tech 3343-2023, *Guidelines for Production of Programmes in accordance with EBU R 128*, Ginebra, noviembre 2023. https://tech.ebu.ch/docs/tech/tech3343.pdf
- Clear-Com LLC, *Interruptible Fold Back, AKA IFB* (Tech Blog del fabricante, 16-03-2021). https://www.clearcom.com/Resource-Library/Details/interruptible-fold-back-aka-ifb
- Clear-Com LLC, *A Comprehensive Guide to Clear-Com Analog and Digital Partyline Systems*, febrero 2018 (© 2018), copia en https://www.ampco-flashlight.com/wp-content/uploads/2019/02/clear-com-partyline.pdf
- EBU R 128 s1, *Loudness Parameters for Short-form Content (adverts; promos, etc.)*, V3, Ginebra, agosto 2020 (1.ª ed. nov. 2014). https://tech.ebu.ch/docs/r/r128s1.pdf
- EBU Tech 3285, *Specification of the Broadcast Wave Format (BWF)*, Version 2.0, Ginebra, mayo 2011. https://tech.ebu.ch/docs/tech/tech3285.pdf
- iZotope, *RX 11 Manual*, módulo «Spectral De-noise» (manual de fabricante). https://docs.izotope.com/rx11/en/spectral-de-noise.html
- Shure Incorporated, Chris Lyons, *Audio Systems Guide for Video and Film Production* (publicación educativa del fabricante, ©2013/©2014). https://content-files.shure.com/Pubs/audio-systems-guide-for-video-and-film-production/audio-systems-guide-for-video-and-film-production-english.pdf
- BOJA núm. 186, de 24-09-2026, bases de la convocatoria RTVA/CSRTV, Anexo I (plazas por centro y puesto). Leído en la copia local de la convocatoria.
- EBU Tech 3347, *Audio over IP – Production Intercoms – Requirements for Interoperability*, Rev. 1, octubre 2012 (primera edición feb. 2011). https://tech.ebu.ch/docs/tech/tech3347.pdf

---

## Tema 4 · Consolas (lo que falta: entradas y salidas de canal, auxiliares pre/post, grupos DCA y de silencio, matrices, escenas, automatización)

Fuente de todo el apartado 4.1-4.6: Yamaha, *CL5/CL3/CL1 V5 Reference Manual*. Es documentación de
fabricante de UN modelo: el redactor debe presentarlo como ejemplo de consola digital, no como norma
ni como lo que usa CSRTV (no consta qué consolas tiene CSRTV).

### 4.1 Canal de entrada y su cadena · Yamaha CL V5, «Signal flow for input channels»

- «The input channels comprise the section that processes signals received from the I/O devices, rear panel input jacks, or slots 1-3, and sends them to the STEREO bus, MONO bus, MIX buses, or MATRIX buses.» Dos tipos: «MONO channels» y «STEREO channels».
- Orden de bloques, literal: «INPUT PATCH» («Assigns input signals to the input channels»); «Ø (phase)» («Switches the phase of the input signal»); «DIGITAL GAIN»; «HPF (High Pass Filter)» («Cuts the region below the specified frequency»); «4 BAND EQ» («A parametric EQ with four bands: HIGH, HIGH MID, LOW MID, and LOW»); «DYNAMICS 1» («gating and ducking, or as an expander or compressor»); «DYNAMICS 2» («compressor, compander, or de-esser»); «INPUT DELAY» («Corrects input signal delay. You can specify up to 1000ms»); «ON (On/off)» («If this is off, the corresponding channel will be muted»).
- Puntos de inserción: «PRE EQ (immediately before the EQ), PRE FADER (immediately before the fader), or POST ON».
- Salida directa (direct out): puntos «PRE HPF (immediately before the HPF), PRE EQ (immediately before the EQ) or PRE FADER (immediately before the fader), or POST ON (immediately after the [ON] key)».
- Compensación de ganancia en previos compartidos por red: con ella activada «the level of the signal output from the I/O device to the audio network will be stabilized. For example, if the FOH console and the monitoring console are sharing an I/O device, or if you are performing digital recording via Dante connections, using this function will maintain the signal output at a constant level from the I/O device to the network even if the analog gain value on the I/O device is changed».

### 4.2 Canales de salida · Yamaha CL V5, «Signal flow for output channels»

- «The output channel section takes the signals sent from the input channels to the various buses, processes them with EQ and dynamics, and sends them to output ports or other buses.»
- «MIX channels: These channels process signals sent from input channels to MIX buses, and output them to the corresponding output port, MATRIX bus, STEREO bus, or MONO (C) bus.»
- «STEREO channel/MONO (C) channel [...] If input channels are in LCR mode, the STEREO (L/R) channels and the MONO (C) channel can be used together as a set of three output channels.»
- Matriz: «MATRIX channel: These channels process the signals sent from input channels, MIX channels, and STEREO/MONO channels to MATRIX buses, and send them to the corresponding output ports.» (Es decir, la matriz mezcla buses ya mezclados además de entradas.)

### 4.3 Envíos auxiliares: bus fijo o variable, pre o post · Yamaha CL V5

- «MIX buses can be either a FIXED type whose send level is fixed, or a VARI type whose send level is variable. The MATRIX buses are all VARI type.» Con bus FIXED «you cannot adjust the send level».
- Punto de envío: «PRE/POST button: Switches the send point of each send-source channel between PRE and POST. If the button is lit, the send point is set to PRE.» En PRE se elige además «PRE EQ (immediately before the EQ) or PRE FADER (immediately before the fader)».
- Envíos en faders: «SENDS ON FADER mode [...] use the faders on the top panel to adjust the level of signals sent to the MIX/MATRIX buses. When using this method, signals sent from all input channels to a specific MIX/MATRIX bus can be adjusted simultaneously.»
- Mezcla menos automática: «The Mix Minus function removes a specific channel signal from the signals sent to the MIX/MATRIX buses. You can use this function to quickly send monitoring signals to a performer or announcer simply by removing his or her audio signal.»
- La regla pre/post, CONFIRMADA en Soundcraft, *Guide to Mixing*, sección 3: «Pre-fade auxiliaries are independent of the fader so that the amount of effect will not change with new fader levels. This means you will still hear the effect even when the fader is at the bottom of its travel.» «It is important to use post fade auxiliary sends for effects units. This is because post fade auxiliaries ‘follow’ the input fader so that when input level changes the amount of effect remains proportional to the new input level.» Aviso: «Effects Return Aux Post Control must be set to minimum or feedback will occur».
- Monitores (Soundcraft, sección 4): «NOTE: Pre-fade rather than post-fade auxiliaries must be used. This is because they are independent of the input faders. If postfade auxiliaries are used, then foldback mix levels will alter with every input fader change made by the FOH engineer. This will annoy the band and may lead to feedback which can damage speakers and headphones.»
- Glosario Soundcraft: «EFFECTS SEND: A post-fade auxiliary output used to add effects to a mix.» «FOLDBACK SEND: A pre-fade auxiliary output used to set up an independent monitor mix for the performers.» «AFL (AFTER FADE LISTEN): A function that allows the operator to monitor a post-fade signal. Used with Aux Masters.» «DIRECT OUTPUT: A pre-/post-fade, post-EQ line level output from the input channel, bypassing the summing amplifiers». «INSERT POINT: A break point in the signal path to allow the connection of external devices». «BUS or BUSS: A defined set of conductors along which signals may travel. A mixer has several busses carrying the stereo mix, the groups, the PFL signal, the aux sends, etc.» «GROUP: An output into which a group of signals can be mixed.» «MUTE GROUPS: A method of combining the on/off status of a selection of channels under a single control button.» «SOLO-IN-PLACE: A function that allows the operator to listen to a selected channel on it's own but complete with all relevant effects, by automatically muting all other inputs.»
- Yamaha, *Get on the Bus* (misma regla, con grabación): «Pre-fader auxiliary sends are independent of the channel fader position and are often used for independent mixes: stage monitors and recording sends.» «Post-fader auxiliary sends depend on the channel fader position and are often used for effects like reverb and delay, aux-fed subwoofers, etc.»
- Matriz (Yamaha, *Get on the Bus*): «Matrix buses allow for the creation of custom mixes that combine multiple input signals in different proportions. These mixes can be sent to various destinations, such as additional speakers or recording devices.» Soundcraft: la consola de sala tendrá «a large number of matrix outputs so that a complex range of speaker clusters can be placed around the auditorium».
- Bus de órdenes (Yamaha, *Get on the Bus*): «Talkback buses are used for communication between the engineer and performers on stage or between different parts of a production team.»

### 4.4 Grupos DCA y grupos de silencio · Yamaha CL V5

- DCA: «CL series consoles feature sixteen DCA groups that enable you to control the level of multiple channels simultaneously.» «A single DCA fader will control the level of all input channels belonging to the same DCA group while maintaining the level difference between the channels. This provides a convenient way in which drum mics, for example, can be grouped.» «DCA group settings are saved as part of the scene.»
- Desde V3.0 el DCA puede agrupar también masters de salida: «you can use the DCA groups for output master channels».
- Silencio: «CL series consoles feature eight mute groups. Mute groups enable you to [...] mute or unmute multiple channels in a single operation.» «Mute groups 1 - 8 can be used with both input channels and output channels.» «You may assign a single channel to more than one mute group.»
- Subgrupo frente a VCA/DCA, CONFIRMADO en Yamaha, *Get on the Bus*: «A sub-group is a grouping of multiple audio channels or tracks that are mixed before being sent to the main mix bus.» Permite «apply processing like EQ or compression collectively». «A VCA is a control mechanism used to adjust the level (volume) of multiple channels simultaneously without affecting their relative balance. VCAs do not actually pass audio signals themselves [...]. Unlike sub-groups, VCAs do not sum audio signals together». «VCA is an analog technology that uses control voltages»; «DCA is a digital technology that uses digital control signals»; «In practical terms, however, VCAs and DCAs function similarly».
- Subgrupos (Soundcraft, sección 1): «These allow the logical assignment of groups of instruments or vocalists so that they may be controlled by just one pair of faders, or even a single fader, once individual instruments’ relative levels have been balanced. They also act as additional outputs with separate volume/level controls».

### 4.5 Escenas, Recall Safe, Focus y Fade · Yamaha CL V5, «Scene memory»

- Definición: «you can assign a name to a set of mix parameter and input/output port patch settings, and store the mix settings in memory (and later recall them from memory) as a "scene."»
- «Each scene is assigned a number in the range of 000-300. Scene 000 is a read-only scene used to initialize the mix parameters. Scenes 001-300 are writable scenes.» (Cifra propia del modelo.)
- Qué guarda una escena: «the position of the top panel faders and [ON] key status, as well as [...] Input/output port patching; Bus settings; Head amp settings; EQ settings; Dynamics 1 and 2 settings; Rack (GEQ/Effect/Premium Rack) settings; Pan/balance settings; Insert/Direct Out settings; On/off status and send level of signals sent to MIX buses; On/off status and send level of signals sent to MATRIX buses; DCA group settings; Mute group settings; Channel link settings».
- Recall Safe: «a function that excludes only specific parameters/channels (DCA groups) from Recall operations. Unlike the Focus Recall function [...], which you can apply to individual scenes, the Recall Safe settings are globally applied to all scenes.» Salvedad: «Channel Link [...] and bus settings are not subject to Recall Safe; they will always be reproduced in the recalled scene.»
- Focus Recall: «lets you specify the parameters that will be updated when you recall a scene. For example, it is convenient to use this if you want to recall only the input channel settings of a certain scene.»
- Fade: «a function that smoothly changes the faders of specified channels and DCA groups to their new values over a specified duration when you recall a scene. The settings of the Fade function are made independently for each scene.»

### 4.6 Escucha, cue y órdenes · Yamaha CL V5, «Monitor and Cue functions», «Talkback and Oscillator»

- Puntos de escucha del cue de entrada: «PFL (immediately before fader), AFL (immediately after fader), or POST PAN (immediately after PAN)». (Completa el PFL de RTVE con AFL.)
- Grupos de cue: «INPUT CUE group», «DCA CUE group» (y los de salida).
- Órdenes: «Talkback is a function that sends the signal of a mic connected to the TALKBACK jack to the desired bus. This is used mainly to convey instructions from the operator or sound engineer to the performers and staff.»
- «When talkback is on, you can use the talkback dimmer to lower the monitor levels other than the talkback signal» (enlaza con el DIM de RTVE).
- Oscilador: la consola incluye «an oscillator that can output a sine wave or pink noise».

### 4.7 Ajuste de ganancia con PFL y posición de los faders · Soundcraft, *Guide to Mixing*, sección 3

- «Input gain is designed to take an audio signal, and adjust it to the level which the mixer understands.» «Ideally the input signal should be as high in level as possible while still leaving a margin of safety to prevent distortion on loud sections. [...] The remaining safety margin is known as Headroom.»
- Procedimiento: «Press the PFL/Solo switch on the relevant input. Adjust gain/input sensitivity until meters read within the yellow [...]. Release PFL/Solo. Repeat for all other inputs.» (La lectura «‘3’ to ‘6’» es de medidores Soundcraft: no generalizar.) «NB: EQ affects gains settings.»
- PFL para ajustar: «PFL solo is very useful for setting proper input preamp levels»; el solo en posición (SIP) «is less good for level setting, but more useful in mixdown situations».
- Faders: «It is important to keep your input faders around the ‘0’ mark for greater control. This is because fader scales are typically logarithmic and not linear». Masters: «Set your master outputs to ‘0’ on the scale».

### 4.8 Modos de automatización · Avid, *Pro Tools Reference Guide* 2025.12, cap. 55

(Automatización de mezcla en DAW y superficies de control; en consolas de directo lo equivalente son las escenas del 4.5.)
- «Automation modes control how a track’s automation data is written and played back.»
- «Off mode turns off automation for all automatable parameters» (volumen, panorama, mute, envíos, plugins, MIDI); «automation data for these parameters is ignored during playback».
- «Read mode plays any automation that was previously written for a track.»
- «Write mode writes automation from the time playback starts to the time it stops, erasing any previously written automation for the duration of the automation pass.»
- «Touch mode writes automation only while a fader or switch is touched or clicked with the mouse. When the fader is released, the writing of automation stops and the fader returns to any previously automated position».
- «Latch mode works in the same way as Touch mode, writing automation only if you touch or move a control. However, unlike Touch, writing of automation continues until you stop playback or “punch out”». «Latch mode is particularly useful for automating Pan controls and plugins on non-touch sensitive rotary controls».
- «Touch/Latch Automation mode places a track’s Volume control in Touch mode and all other automatable controls in Latch mode» (sólo Ultimate y Studio).
- Trim: ajusta «existing track volume and send level automation data in real time. Pan, mute and plugin automation cannot be trimmed in this manner.» «When writing automation in Trim mode, fader moves write relative rather than absolute values.»
- Los nombres (Read, Write, Touch, Latch, Trim) son de Pro Tools; otros DAW usan nombres parecidos, pero sólo se ha leído Pro Tools.

### 4.9 Nivel de alineación en equipos digitales · EBU R 68-2000

(Completa el «−18 dBFS» que ya da ing-tec-teleco/12.)
- «The EBU recommends that, in digital audio equipment, its Members should use coding levels for digital audio signals which correspond to an alignment level which is 18 dB below the maximum possible coding level of the digital system, irrespective of the total number of bits available.» Nota 2: 18 dB es «corresponding to a ratio of 1:8 (18.06 dB)».
- Razones del considerando: la señal de alineación tiene un nivel «9 dB (or 8 dB in some organizations) below the permitted maximum level of the audio programme» (términos de UIT-R BS.645); con medidores cuasipico «the true programme peaks can be 3 dB greater than those indicated; When operator errors are taken into account the true peaks may occasionally be 6 dB greater than indicated or 15 dB above alignment level».
- «the only reliable method to specify a level in a digital signal is by reference to the maximum digital codes allowed by the number of bits in use».
- Grabación: «linear coding using no pre-emphasis and with a resolution of at least 16 bits in accordance with ITU-R Recommendation BS.646».
- La equivalencia analógica «−18 dBFS = 0 dBu» NO aparece en R 68: no atribuírsela.

---

## Tema 6 · Captación en informativos, exteriores, eventos, deportes (lo que falta: informativos y eventos; estrategia de mezcla en deportes y espectáculos)

Aviso de alcance de la fuente: Shure dice de su propia guía «This booklet is not designed for the professional film or television producer». Úsese para principios de captación, no como práctica de televisión profesional. La parte de mezcla de deportes y espectáculos está en 8.2 (EBU Tech 3343-2023, §3.5): el redactor del 6 la cita desde allí.

### 6.1 Informativos: micrófono de mano omnidireccional y ambiente · Shure, *Audio Systems Guide*

- «The handheld microphones used by field news and sports reporters are usually omnidirectional, allowing the reporter and interviewee to be picked up by one microphone held between them, and delivering a certain amount of ambient sound.»
- Por qué algo de ambiente: «an omnidirectional mic picks up some of the ambience of the situation, which can help to reinforce the visual setting. If the scene takes place on a street corner, some traffic sound is desirable, as long as it does not overwhelm the dialogue.»
- Inconvenientes: «they may also pick up undesired background noises (doors slamming, excessive traffic noise, people talking behind you, etc.)» y «greater amounts of room reverberation».
- Entrevista en movimiento: «the interviewer can hold an omnidirectional handheld mic attached to a plug-on wireless transmitter, similar to those used by TV news reporters in the field». Para dos que hablan largo, «two wireless lavaliers and two receivers».

### 6.2 Redundancia en directo: doble micrófono · Shure, *Audio Systems Guide*

- «In a live event, even a remote chance that the microphone might fail constitutes an intolerable risk. For this reason, a news anchor or key presenter may wear two lavalier microphones for redundancy. Only one mic is used at a time; if the primary mic fails, the backup mic channel can be turned up immediately. Double-miking with lavalier microphones is usually achieved with a special tie clip or bar that holds two microphones.»

### 6.3 Niveles y pista de seguridad · Shure, *Audio Systems Guide*

- «Set the level to accommodate the loudest expected volume, since you can’t adjust it during a take. Also be aware that talkers often speak louder while presenting than they do when saying “check 1-2-3” during setup.»
- «Some audio recorders can record a duplicate “safety” track at a reduced level, to guard against unexpectedly loud levels. A tone generator can be useful for setting consistent audio levels at different devices in the audio chain (e.g. wireless receiver, mixer, audio recorder, camera).»
- Pocos micrófonos: «Use the fewest microphones necessary for the situation. [...] Excess mics mean more background noise pickup, a greater chance of a “tin can” sound (caused by sound reaching more than one open microphone)».
- Distancia: la ley del cuadrado inverso implica que «the talker-to-mic distance must be cut in half to cause a significant improvement in sound quality».

### 6.4 Eventos: mesas, preguntas del público, visita previa · Shure, *Audio Systems Guide*

- Regla 3 a 1: «The distance between open microphones should be at least three times the distance from each microphone to the nearest talker.» Si no, «a hollow, “tin can” sound, caused by the same sound reaching more than one microphone at slightly different times». Y: «it’s best to turn off microphones that are not being addressed. This could be done either by a live operator or with a voice-activated mixer.» (Comprobar si RTVE sonido/05 ya la da: grep no la encontró.)
- Preguntas del público: «there is no truly effective way to do it»; dos opciones: «bring the audience member to a microphone, often by placing a unidirectional microphone on a stand in the aisle» o «bring a microphone to the audience member» con inalámbrico. El cañón: «usually doesn’t work very well if the questions must also be fed to the PA system in the room (because of feedback)»; «Shotgun mics are not very effective beyond 20 feet in a large crowded room».
- Mesa de reunión: «The ideal approach is to individually mic each participant and record each microphone’s output separately on a multi-track recorder.»
- Micrófonos ajenos en el evento: «if there are other people’s mics at the event, you can expect that one of these mics will be used instead of yours for something important».
- Visita técnica: «The most important thing you can do to guarantee good audio is to take the time to conduct a site visit in advance of the event.» Preguntas al recinto, entre ellas qué equipo inalámbrico, «in-ear monitors, or intercom systems» hay ya instalado «and what frequency does it operate on that needs to be avoided».
- Antes del evento: «Always do a “walkaround” before the event begins».

### 6.5 Deportes y espectáculos: estrategia de mezcla

- Ver 8.2 (EBU Tech 3343-2023, §3.5.1 y §3.5.2): comentaristas «at −24 LUFS» para dejar sitio al público; en espectáculos, público «around Target Level» y presentador «fly above and below»; en musicales manda la música.
- Tech 3326 (7.2) da el retorno de un comentario de fútbol como ejemplo de contribución bidireccional con retorno de banda estrecha en que «Latency is not an issue».

---

## Tema 7 · Sonido en radio (lo que falta: códecs IP y norma ACIP, streaming, podcast)

### 7.1 Por qué existe ACIP · EBU Tech 3326 Rev. 4 (nov. 2014), §1.1

- «Increasingly, broadcasters are using IP connections for the purposes of streaming high-quality broadband audio to their production centres. This is in part accounted for by the fact that several countries are withdrawing ISDN services, which have been heavily used for contribution in the past.»
- «About 15 to 20 manufacturers currently provide units capable of transferring audio over both ISDN and IP connections, and efforts must be made to achieve interoperability between units from different manufacturers.»
- Alcance: «a minimum set of requirements necessary to ensure interoperability between equipment intended for the transport of contribution-quality audio over IP networks» (Scope).
- Vocabulario normativo: «MUST and SHALL identify mandatory elements»; «SHOULD and RECOMMENDED identify elements that are not mandatory, but whose implementation is advisable»; «MAY and OPTIONAL identify facultative elements» (Scope).
- Buenas prácticas en otro documento: «Best practices and other considerations not directly linked to interoperability are published in EBU Tech 3329» (§1.4). (Tech 3329 no leído.)

### 7.2 Tipos de contribución y de equipo · Tech 3326, §1.2 y §1.3

- Tres tipos, literal: «Unidirectional with no return channel (example: contribution by satellite).» / «Bidirectional where the return audio is narrowband and for the purposes of cueing the contribution (examples: concert, football commentary). Latency is not an issue.» / «Bidirectional with bidirectional broadband audio (examples: interview, discussion). Latency is an issue.»
- Equipos: «General contribution equipment: Equipment meant for all type of contribution (fixed or remote).» / «Portable contribution equipment: Equipment meant mainly for monophonic speech contribution at low bitrates.» Los requisitos de los portátiles son «less stringent».
- Cuatro áreas que regula (§1.4): transporte sobre IP («including port definition and packet loss recovery mechanisms»), «Audio coding algorithms to be implemented», «Audio frame encapsulation», «Signalling: defines connection setup and termination procedure».

### 7.3 Transporte · Tech 3326, §2

- «IP version 4 as defined in RFC791 MUST be used.» «IP version 6, as defined in RFC2460, SHOULD be supported.» Multicast: «SHOULD be available for sending and receiving according to RFC1112».
- «Realtime Transport Protocol (RTP) over UDP SHALL be used as transport protocol» según RFC3550 y RFC3551. RTCP: «RECOMMENDED».
- Puertos: «Port 5004 (RTP) and port 5005 (RTCP) SHOULD be used as default ports.»
- Corrección de errores: FEC según «RTP Payload Format for Generic Forward Error Correction» (RFC2733/5109); retransmisión con el perfil RFC4585.
- TCP: «MAY be implemented in addition to RTP»; puerto por defecto 5004 para «RTP over TCP».

### 7.4 Códecs · Tech 3326, §3

**Obligatorios (§3.1)**, literal:
- G.711: «ITU G.711 audio coding standard with a bitrate of 64 kbit/s SHALL be implemented.» Tipos de carga «‘PCMA’ for A-law with RTP Payload type ‘8’ and ‘PCMU’ with RTP Payload Type ‘0’ for mu-law». «20 ms of audio per RTP packet SHOULD be used as default».
- G.722: «ITU G.722 audio coding standard with a bitrate of 64 kbit/s SHALL be implemented.» Tipo de carga 9. Rareza que puede preguntarse: «Even though the sampling rate for G.722 audio is 16 kHz, the RTP clock rate for the G.722 payload format is 8 kHz because this value was erroneously assigned in RFC1890».
- MPEG Layer II: «ISO/IEC 11172-3 MPEG-1 Layer II and ISO/IEC 13818-3 MPEG-2 Layer II coding SHALL be implemented.» Tipo de carga 14 o dinámico; reloj RTP «always 90 kHz». Tabla de velocidades recomendadas de 32 a 384 kbit/s a 16, 24 (MPEG-2), 32 y 48 kHz; leyenda «M = Mono, JS = Joint-Stereo, S = Stereo»; a 32 kHz, 320 y 384 kbit/s «frame too large».
- PCM 16 bits: «MIME Subtype name: L16 (RFC3555) Linear audio. Sampling frequencies to be supported: 32 kHz, 48 kHz». «4 ms of audio per RTP packet SHOULD be used as default». «OPTIONAL for portable units».
- PCM 12, 20 y 24 bits: «DAT12, L20, L24»; «12-bit per sample quantization is OPTIONAL»; también opcional en portátiles.

**Recomendados (§3.2)**: «MPEG-4 AAC Low Complexity Profile, MPEG-4 AAC-LD» (RFC3640; «High bitrate AAC profile (AAC-hbr) MUST be supported and SHOULD be used») y «Standard/Enhanced APT-X» («ADPCM based format», RFC7310).

**Opcionales (§3.3)**: MPEG-1/2 Layer III; MPEG-4 HE-AACv2; Opus («Free Open source voice/music codec with bitrates ranging from 6 kbit/s to 510 kbit/s as defined in RFC6716»); AMR-WB/AMR-WB+ («AMR-WB (G.722.2)»).
- Regla general: «audio formats must have an RTP payload format defined and registered at IETF» (§3.3.5).

### 7.5 Señalización · Tech 3326, §4

- «Session Description Protocol according to RFC4566 MUST be used for session description.»
- Enlaces unidireccionales multicast: «SAPv1 according to RFC2974 SHOULD be supported.»
- «SIP, according to RFC3261, MUST be used as the signalling method for bidirectional links. The SIP requests ‘INVITE’, ‘ACK’, ‘BYE’ and ‘OPTIONS’ MUST be supported for basic communication. SIP registrar MUST also be supported so ‘REGISTER’ message MUST be supported.»
- «5060 MUST be used as a default port for establishment.»
- Negociación: «the model described in RFC3264 (An Offer/Answer Model with the Session Description Protocol) MUST be used. User SHOULD be able to define prioritisation of codec.»
- Cambio de códec en llamada: «the sender MUST send a new SIP INVITE command with SDP signalling the new codec to be used. The receiver replies with a SIP ACK command».

### 7.6 Perfiles · EBU Tech 3368 v1.0 (nov. 2014)

- Para qué: «audio engineers or reporters should not be required to specify these parameters in detail; instead, it would be more useful to be able to select a profile to use for this particular connection» (§1).
- Definición: «A profile is a set of parameters describing how to transmit and receive audio streams and for the decoder to successfully decode the audio, based on the parameters sent.» «It must be possible to store a number of pre-configured profiles in all user agents.» (§2)
- Perfil asimétrico: «specifies different parameter values for the sent and received streams»; ejemplo, «a DSL line with low upload capacity and high download capacity»; se señala con «a=sendonly and/or a=recvonly» (§2.1).
- Parámetros de un perfil (tabla 1): número y nombre de perfil, algoritmo, velocidad, frecuencia de muestreo, modo de canal, versión, «RX jitter buffer», «Packet length», «QoS-Recommendation», «Protection».
- Atributo propio: «a=ebuacip:»; «This document defines version 0» («a=ebuacip:version 0»). Parámetros nuevos: «jb (jitter buffer)», «jbdef», «plength (packet length)», «qosrec», «protp».
- Búfer de fluctuación: «If the jitter buffer is too small, packets can fill up the buffer quicker than they can be played out, causing packets to be lost [...]. If the jitter buffer is too large, all packets can expect to be safe, but then the total delay in the system may be unacceptably high, particularly for two way conversations» (§3.4). Adaptativo (mínimo y máximo) o estático (fijo) (§3.4.1-3.4.2).
- Caso práctico literal: un equipo en la red corporativa con búfer fijo de «six milliseconds» llamado desde una wifi de hotel: «this call will fail or at the very best be full of audio glitches, since the stream is transported over the public Internet» (§3.4.3).
- Rechazo: si no se acepta ninguna opción, «"488 Not Acceptable Here" response, as defined in RFC3261» (§3.4.4.1).
- Calidad de servicio: «The DiffServ method as described in RFC2474 shall be implemented. The DS field is the 6 most-significant bits of the deprecated TOS field» (§3.6).
- Protección: «Media duplication redundancy», «Forward error correction», «Multiplexing protection» (§3.7.2).

### 7.7 Streaming: sonoridad de distribución · AES TD1008.1.21-9 (24-09-2021)

- Identificación: «AESTD1008.1.21-9 (supersedes TD1004)». Es documento técnico (recomendación), no norma.
- Pico: «For all content, it is recommended that the Maximum True Peak level not exceed -1 dBTP at the codec input of lossy-encoded streams.»
- Tabla 1, literal (Distribution Loudness en LUFS / tolerancia superior en LU): «Assorted — Speech is measurable: -18 / +1 (Dialog Integrated Loudness)»; «Speech is not measurable: -18 / +2 (Integrated loudness)»; «Music — Track-normalized: -16 / +0.2»; «Album-loudest track (e.g., on-demand music services): -14 / +0.2»; «Interstitial: -18 / +0.2»; «Virtual Assistant: -18 / n/a».
- Nota 1 de la tabla: «Assorted» «applies to radio-style streams, musical concert performances, podcasts containing speech, music and/or effects elements». Nota 7: «Interstitial Content such as commercial advertising, public service announcements, promotional material».
- Tabla 2, por formato: «News/Talk -18 LUFS; Pop music -16 LUFS; Mixed format -17 LUFS; Sports -17 LUFS; Drama -18 LUFS». Fórmula: «Distribution Integrated Loudness = -16 − [2 × (SpeechPercentage/100)] (LUFS)»; «approximately 1 LU is considered a just noticeable loudness difference».
- Voz frente a música: «listener experience can be improved by normalizing music 2 or 3 LU higher than speech».
- Relación con la emisión: se recomienda revisar el documento «lowering its Distribution Loudness recommendations by 6 LU. This will harmonize this document with others such as EBU R 128, ATSC A/85, ANSI/CTA-2075 and AES71-2018, which recommend -23 to -24 LUFS». Y producir y archivar «at a loudness of -24 LUFS or lower and then remastered for distribution».
- «LUFS and LKFS are identical units of measurement as specified in ITU-R BS.1770.»

### 7.8 Streaming: el protocolo HLS · IETF RFC 8216 (agosto 2017)

- «HTTP Live Streaming provides a reliable, cost-effective means of delivering continuous and long-form video over the Internet. It allows a receiver to adapt the bit rate of the media to the current network conditions in order to maintain uninterrupted playback at the best possible quality.» Ofrece «multiple renditions of the same content, such as audio translations».
- «A Playlist is either a Media Playlist or a Master Playlist. Both are UTF-8 text files containing URIs and descriptive tags.» «A Media Playlist contains a list of Media Segments, which, when played sequentially, will play the multimedia presentation.»
- «Clients should switch between different Variant Streams to adapt to network conditions.»
- Estatus: «This document is not an Internet Standards Track specification; it is published for informational purposes.» «It describes version 7 of this protocol.»

### 7.9 Podcast: requisitos de audio de una plataforma · Apple Podcasts for Creators

(Requisitos de UNA plataforma comercial, no norma; útil como ejemplo de «entrega» de un pódcast.)
- Suscripción: «Apple Podcasts Connect accepts WAV, FLAC, or MP3 audio». «Single-channel audio will not be accepted for WAV or FLAC files.»
- MP3 mono: mínimo «44.1 kHz», «32 kbps»; recomendado «44.1/48 kHz», «96–128 kbps». MP3 estéreo: mínimo «64 kbps»; recomendado «128–256 kbps».
- RSS: «For RSS feeds, Apple Podcasts accepts MP3 or AAC formats.» «For the same bit rate, AAC will result in better audio quality.» «we strongly recommend using AAC instead of MP3».
- Sonoridad: «we recommend that the audio signals are preconditioned so the overall loudness remains around -16 dB LKFS, with a +/- 1 dB tolerance, and that the true-peak value doesn’t exceed -1 dB FS. The LKFS and true-peak values are calculated according to the ITU-R BS.1770-5 recommendation.» «The preconditioning steps need to occur before the encoding process [...] audio compression algorithms typically don’t modify the loudness and might clip the signal».
- Metadatos: se pueden incrustar sonoridad y picos en «the ID3 tags of an MP3 file or in the header of an MP4 file».
- Contraste que puede preguntarse: pódcast −16 LKFS (Apple) / −18 LUFS voz (AES TD1008) frente a −23 LUFS de emisión (EBU R 128, tema 13).

### 7.10 El híbrido: de 2 a 4 hilos · Clear-Com, *Partyline Guide* (feb. 2018)

(Completa lo que RTVE da de híbridos telefónicos; la fuente es de intercom pero el principio es el mismo y lo dice: «Hybrids are also used in intercom systems as interfaces to telephone networks».)
- «The term hybrid refers to a device that converts two-wire to four-wire audio and vice versa. Analog hybrids initially used transformers [...] and later used op-amps [...]. Digital hybrids with digital signal processing (DSP) chips are most commonly used».
- «we evaluate this with a metric called ‘trans-hybrid loss’. This is a measure of the loss or isolation between the transmit and the receive ports on the four-wire side of the circuit – in this case ‘loss’ being desirable up to some amount. Trans-hybrid loss depends on signal cancellation accomplished through defining the line impedance and mirroring it in a balanced network.»
- «Null: Nulling refers to adjustments made in balancing a network to achieve greater trans-hybrid loss [...]. Modern hybrids are digital, thus capable of auto-nulling.»
- «There should be no component of the talk signal in the listen signal. This is accomplished by adding an inverse polarity copy of the talk to the Listen.» «High gain between the send and receive poses a risk of oscillation or ‘howling’».

---

## Tema 8 · Sonido en televisión (lo que falta: intercom sobre IP, IFB, cámaras, mezcla para emisión)

### 8.1 Intercom de producción · EBU Tech 3347 Rev. 1 (oct. 2012)

- «Intercom systems are used to establish real-time communication networks between different locations. For instance, a live TV event requires interconnection with one or more studios, one reporter in the field and one OB van to the main control room. This system will use one or more intercom matrices, many dedicated panels, some handsets and phones.» (§1.1)
- «broadcasters used to transport intercom audio over ISDN or PSTN lines through dedicated interfaces but more and more also use IP interfaces».
- Tipos de señal (§1.2), literal: «1. pure intercom a. full duplex point to point communication b. conference call (alternative point-to-multipoint) 2. mix-minus a. half-duplex b. or return feed of a full-duplex communication 3. commentary feed a. half –duplex b. main feed of a full-duplex communication».
- Usos cotidianos (§1.2): «Communication between two studios (matrix-to-matrix)», «between one studio and an OB van», «with a remote studio (matrix to matrix or matrix to panel)», «with a VoIP Phone inside the company», «with a reporter on the field (matrix-to-phone / matrix-to-softphone)».
- Dispositivos (§1.3): «IP interface integrated into the main matrix system», «integrated into a peripheral device», «external dedicated device», «software application».
- Retardo (§1.5): «It would be outside the scope of this document to try to set latency. However, as a best practice [...] a survey done with users of intercom systems has shown that such end-to-end latency value are expected: Less than 100 ms for remote intercom system; Less than 50 ms for in-house, internal intercom system». «ITU-T G.114 figures on end-to-end delay for normal phone conversation can be used as guidelines.» (Es encuesta de usuarios, no requisito: decirlo así.)
- Transporte: igual que ACIP, «Real-time Transport Protocol (RTP) over UDP SHALL be used» (§2.2).
- Códecs obligatorios (§3.1): G.711 y G.722, ambos «64 kbit/s SHALL be implemented». Recomendados (§3.2): Speex («designed for speech»; banda estrecha 8 kHz y ancha 16 kHz) y «G.729 [...] toll quality speech at a reasonably low bit rate of 8 kbit/s».


### 8.2 Mezcla para emisión en directo · EBU Tech 3343-2023

(Posible solape con el tema 13, sonoridad: RTVE sonido/14 no recoge Tech 3343 según grep; el redactor del 8 toma sólo lo de mezcla en directo y el del 13 lo demás.)
- Tolerancias: en postproducción «a general tolerance of ±0.2 LU around the Target Level of −23 LUFS is acceptable» (nota 2: introducida «in EBU R 128 revision 3 (2020)»). «Especially for live programmes it is challenging (if not a matter of luck) to achieve Target Level at the end of the mix. Therefore, a tolerance of ±1.0 LU around the Target Level of −23 LUFS is acceptable for such programmes».
- Procesador de sonoridad a la salida del control central: «the broadcast system shall signal to the Loudness Processor when loudness-compliant content is played [...]. The processor should then switch to Bypass Mode or to a preset that only applies safety True-peak limiting. Such signalling may be performed via GPIO or control data network systems.» (§2.4)
- En directo: «A Loudness Processor might also be used for live production, in the spirit of “harmonizing the source”. With appropriate settings such a processor can aid the mix engineer to actually tame some of the unpredictably loud parts of a live programme.» Aviso literal: «Don’t produce loudness sausage!»
- Escucha: «Loudness levelling encourages to mix ‘only by ear’ - after setting levels and a fixed monitor gain.» Si antes se mezclaba a unos −20 LUFS, «the listening level should be increased by 3 dB» (§3.1).
- Deportes (§3.5.1): «A few goals in the last 15 minutes of a football match, for example, can boost the integrated loudness level considerably». «it is advisable to have the voice loudness level(s) of the commentator(s) sit a bit below Target Level (for example, at −24 LUFS), so that unexpected crowd noise has more room to move.» Deportes tranquilos: «For sports with a rather quiet atmosphere (for example, golf), the relative gate [...] will eliminate most of the pauses of the commentary».
- Espectáculos (§3.5.2): «the audience is as important a signal as the presenter(s)! Consequently, it may be more advantageous to balance the audience around Target Level – and have the presenter fly above and below.» En musicales «the music is the most important signal»; la «comfort zone» del oyente es «about +3/−5 LU around Target Level». Show muy vivo: «slightly increase the listening level / monitor gain (1-2 dB)».
- «The True-Peak Level in production shall not exceed −1 dBTP.»
- Alineación (§8.1): tono de «1 kHz at a level of −18 dBFS» (remite a R 68-2000); con el máximo de pico verdadero «the recommended PML of −9 dBFS in ITU-R BS.645 becomes obsolete». El tono de −18 dBFS «will read as −18 LUFS on a loudness meter [...] (or +5 LU on the relative EBU mode scale)» si está en fase en ambos canales; «The EBU therefore recommends using a peakmeter for alignment.»
- Nivel de escucha de referencia (§8.2): cada altavoz principal a «LLISTref = 73 dBC SPL, using a 500-2000 Hz reference noise signal at −23 LUFS»; medidor «C-weighted slow response»; diferencia entre canales ≤ 1 dB, y entre frontales «less than 0.5 dB SPL»; LFE «+10 dB gain relative to the same limited frequency band in a main channel».

### 8.3 IFB: sus tres elementos · Clear-Com, *Interruptible Fold Back, AKA IFB* (16-03-2021)

(RTVE realizacion-tv/18 ya da qué es el IFB y cómo se distingue del intercom; esto añade su composición.)
- «Interruptible Fold Back, or IFB, is a type of simplex intercom for sending a program feed and interrupt (cue) audio on IFB lines for a talent to monitor. The IFB line is comprised of three elements: Program Audio, Interrupt (Cue) Audio, and a Dip or Mute control. IFB typically uses an earpiece, an external headphone box (to permit the talent to control the audio foldback level), a program source and a control station.»
- Escucha del control: «Monitor loudspeakers in control areas can be connected to the IFB system such that they are muted or dimmed when the IFB is active. This will prevent acoustic leakage of control room monitor audio into the IFB during an interrupt.»
- Usos: «IFB is used to cue on-camera announcers and is used between studio director, on-scene reporters, and the in-studio anchor in broadcast television. Similarly, sports broadcasting uses many channels of IFB to cue announcers in various locations on the field and in booths.»

### 8.4 Intercom de línea compartida (partyline), 2 y 4 hilos, cámaras · Clear-Com, *Partyline Guide* (feb. 2018)

- «an analog partyline intercom, also commonly referred to as a 2-wire system, is a communications system where the path is the same for both talk and listen. The name “partyline” (PL) came from the original telephone systems where more than one subscriber shared the same line [...]. Therefore, partyline intercoms are always full-duplex and are commonly non-private.» Ejemplo: «An example in broadcast would be camera operators on a camera PL».
- Cableado Clear-Com: cable de micrófono de dos conductores apantallado, XLR de 3 pines; «One wire, connected to pin 2, carries the DC power (30 Volts, i.e.±15V) [...]. The other wire, connected to pin 3, carries the 2-way (duplex) audio information. The shield, connected to pin 1, acts as a common ground.» (Es el sistema de UN fabricante; RTS usa otro reparto: no generalizar.)
- «every intercom circuit starts out as a 4-wire circuit; i.e., headset earphone/microphone, or separate microphone/loudspeaker.» «Four-wire audio is defined as a pair of conductors carrying an input/receive signal and a second pair carry the output/send signal.»
- Cámaras: «There is no standard design for camera intercoms among different camera manufacturers.» «The majority of large installations and virtually all mobile units use camera isolate systems. A camera isolate system allows an operator (usually the video operator or technical director) to have private communications with any of the camera operators for set-up or maintenance purposes without interfering with ongoing communication between the other cameras and the director.»
- Conexión de la CCU: es mejor «to use the four-wire interface that is available on most camera control units (CCU) instead of a two-wire interface when connecting CCUs to a matrix intercom system». «It is always best to interface each camera individually»; si se juntan en paralelo, «the worse the partyline impedance characteristics become». Trampa del conector de 3 pines de la CCU: «The +/hot & -/cold pins are a 2-wire partyline, with the “common” simply being a shield/ground.»
- NO CONFIRMADO: definición de intercom «de matriz» (punto a punto, paneles con teclas) en fuente de fabricante; Tech 3347 (8.1) sólo la nombra («intercom matrices, many dedicated panels»). RTVE realizacion-tv/18 describe el panel.

---

## Tema 9 · Grabación, edición y postproducción (lo que falta: cuñas y piezas cortas, fichero de entrega BWF, limpieza, entrega)

### 9.1 Cuñas, promociones y piezas cortas: la norma de sonoridad · EBU R 128 s1, V3 (agosto 2020)

(No está en RTVE sonido/14. Es lo que convierte «cuñas, ráfagas y continuidad» en materia técnica.)
- Por qué existe: «Especially for short-form content like advertisements (commercials) and promos (as well as interstitials etc.) there is a need to give guidance using the parameter Maximum Short-term Loudness in addition to the basic parameters Programme Loudness and Maximum True Peak Level.» Sirve para evitar «overly dynamic short-form programmes, which would lead to audience complaints».
- Definición: «Short-form content: A programme of short duration (up to approximately 2 minutes), typically shorter than 30 seconds; In addition to advertisements (commercials) and promotional items also interstitials, stingers, bumpers and similar very short items belong to that category.»
- «Programme: An individual, self-contained audio-visual or audio-only item to be presented in Radio, Television or other electronic media. An advertisement (commercial), trailer, promotional item (‘promo’), interstitial or similar item shall be considered to be a programme in this context.» (Vale para radio: dice «audio-only».)
- Recomendaciones literales: «b) that the Programme Loudness Level shall be normalised to a Target Level of −23.0 LUFS. [...] a tolerance of ±0.2 LU is allowed»; «d) that the Short-term Loudness Level (measured in compliance with EBU Tech 3341) shall not exceed −18.0 LUFS (+5.0 LU on the relative scale). [...] a tolerance of +0.2 LU is allowed»; «f) that the audio signal shall generally be measured in its entirety, without emphasis on specific foreground elements such as speech, music or sound effects»; «g) and that the True Peak Level of the programme shall not exceed −1 dBTP [...]. The measurement tolerance is ±0.3 dB».
- Salvedad c): el nivel puede normalizarse por debajo de −23 «on purpose. This exception shall be clearly indicated to ensure that such a lower Programme Loudness Level is not compensated».
- Rango de sonoridad: «The measure ‘Loudness Range’ is not useful for short-form content. [...] Therefore, a maximum and/or minimum value for Loudness Range shall not be specified for programmes of this length/genre.»
- Historia: 1.ª ed. noviembre 2014; enero 2016 «V2; Simplification, removed alternative Maximum Momentary Loudness limit»; agosto 2020 «V3; Addition of tolerances (for QC and True-peak)».
- Para internet (T7): AES TD1008 da «Interstitial: -18 LUFS / +0.2».

### 9.2 El fichero de entrega: BWF y su cabecera · EBU Tech 3285 v2.0 (mayo 2011)

(RTVE sonido/09 ya dice qué es un BWF y que lleva marca de tiempo; esto da la estructura y las versiones.)
- «The Broadcast Wave Format (BWF) is a file format for audio data. It can be used for the seamless exchange of audio material between different broadcast environments and between equipment based on different computer platforms.» «The Broadcast Wave Format is based on the Microsoft WAVE audio file format, to which the EBU has added a “Broadcast Audio Extension” chunk.»
- Versiones: «Version 0» publicada «in 1997 as EBU Tech 3285»; «Version 1 differs from Version 0 only in that 64 of the 254 reserved bytes in Version 0 are used to contain a SMPTE UMID»; «Version 2 is a substantial revision of Version 1 which incorporates loudness metadata (in accordance with EBU R 128)». Compatibilidad: «Version 2 is backwards compatible with Versions 1 and 0».
- Campos de la extensión «bext», literal: «Description[256] /* «Description of the sound sequence» */», «Originator[32] /* «Name of the originator» */», «OriginatorReference[32]», «OriginationDate[10] /* «yyyy:mm:dd» */», «OriginationTime[8] /* «hh:mm:ss» */», «TimeReferenceLow / TimeReferenceHigh /* First sample count since midnight */», «Version», «UMID_0 ... UMID_63», «LoudnessValue /* Integrated Loudness Value of the file in LUFS (multiplied by 100) */», «LoudnessRange», «MaxTruePeakLevel», «MaxMomentaryLoudness», «MaxShortTermLoudness», «CodingHistory[]».
- Sincronía: «TimeReference: These fields shall contain the time-code of the sequence. It is a 64-bit value which contains the first sample count since midnight. The number of samples per second depends on the sample frequency».
- Historial: «CodingHistory: [...] Each string shall contain a description of a coding process applied to the audio data. Each new coding application shall add a new string».

### 9.3 Limpieza: reducción de ruido por perfil · iZotope, *RX 11 Manual*, «Spectral De-noise»

(Documentación de UN producto comercial: sirve para explicar el principio, no como norma.)
- «Spectral De-noise is designed to remove stationary or slowly changing tonal noise and broadband hiss by learning a profile of the offending noise and then subtracting it from the signal. It can be useful for tape hiss, HVAC systems, outdoor environments, line noise, ground loops, camera motors, fans, wind, and complex buzz with many harmonics.»
- Perfil: «Make a selection of the longest section of noise you can find in your file (ideally a few seconds in length).» «Manually learned noise profiles are best suited to removing or reducing noise that is constant and continuous». Modo adaptativo para ruido cambiante: «recordings in outdoor environments, traffic noise, or ocean waves».
- Umbral: «Higher threshold settings reduce more noise, but also suppress low-level signal components.»
- Reducción tonal y aleatoria por separado: «tonal parts (such as hum, buzz or interference) and random parts (such as hiss)». Aviso: «Strong suppression of noise can also degrade low-level signals, so it is recommended to apply only as much suppression as needed».
- Artefactos: la sustracción espectral «can produce musical noise artifacts, resulting in a “chirpy” or “watery” sound during heavy processing»; el «wide band gating» da «bursts of noise right after the signal falls below the threshold».
- Otros módulos de limpieza del mismo producto (sólo nombres, índice del manual): «De-click», «De-clip», «De-crackle», «De-ess», «De-hum», «De-plosive», «De-reverb», «De-rustle», «De-wind».

### 9.4 Entrega: sonoridad del programa terminado

- Postproducción: tolerancia «±0.2 LU around the Target Level of −23 LUFS» y la corrección es «a simple corrective static gain calculation» (Tech 3343-2023, §3.1 y §3.2; ver 8.2). «Typically, offline loudness meters perform both the measurement as well as the correction.»
- Archivo: producir y archivar «at a loudness of -24 LUFS or lower» y remasterizar para internet (AES TD1008; ver 7.7).

---

## Lo propio de CSRTV que consta en documento publicado

- Único dato encontrado: el reparto de plazas de «OPERADOR/A DE SONIDO» en el Anexo I del BOJA núm. 186 (24-09-2026), todas en la columna CSRTV: Algeciras 1, Almería 1, Cádiz 1, Córdoba 2, Granada 2, Jaén 2, Jerez 1, Málaga 3, Sevilla 8 (suma 21, coincide con las 21 plazas del puesto 2.28). Huelva y Madrid no tienen plaza de este puesto. Sirve para decir, sin inventar, que el puesto se reparte entre la sede y los centros territoriales; NO dice qué hace cada centro.
- No se ha encontrado ningún documento publicado de RTVA/CSRTV sobre consolas, códecs, intercom, sistema de continuidad ni procedimientos de sonido. Una búsqueda web devolvió sólo resúmenes de ofertas de empleo de terceros (andaluciaorienta.net), que no son fuente válida.

## Lo que no se pudo confirmar (y no debe afirmarse)

1. T4 · Equivalencia «−18 dBFS = 0 dBu» (o +4 dBu): no está en EBU R 68 ni en Tech 3343. No atribuirla a la EBU.
2. T4 · Nivel nominal de línea profesional «+4 dBu» frente a doméstico «−10 dBV»: no leído en ninguna fuente de esta fase.
3. T4 · Modos de automatización de otros DAW (Nuendo, Logic, Reaper): sólo se leyó Pro Tools; no generalizar los nombres más allá de «Pro Tools usa...».
4. T4 · Ventajas/inconvenientes «analógica frente a digital» más allá de lo que da RTVE (ing-sup-teleco/12): no se buscó fuente nueva.
5. T6 · Práctica profesional de informativos de televisión (multiplicadores de prensa o «press box», reparto de señal en ruedas de prensa, mochilas y sonido en conexiones en directo): no hallada en fuente publicada. La guía Shure declara no ser para televisión profesional.
6. T6 · Captación en ficción, musicales y documentales: la cubre RTVE (sonido/12, realizacion/09); no se investigó más.
7. T7 · EBU Tech 3329 (buenas prácticas ACIP): citada por Tech 3326 pero no leída. Comprobar si hay revisión de Tech 3326 posterior a la Rev. 4 (2014): la descargada el 25-09-2026 de tech.ebu.ch es la Rev. 4.
8. T7 · Protocolos de contribución por internet no EBU (SRT, RIST) y de ingesta (RTMP): no leídos en esta fase. No mencionarlos como norma.
9. T7 · Definición de «pódcast»: no hay fuente normativa; Apple da requisitos de su plataforma, no una definición. RAE (dle.rae.es) bloqueó el acceso (403): tampoco se pudieron leer «cuña», «ráfaga», «sintonía», «cortinilla» ni «careta». Los términos de radio los da RTVE sonido/12 y produccion/11.
10. T8 · Definición de intercom de matriz (punto a punto) en fuente de fabricante: no leída. RTVE realizacion-tv/18 describe el panel y el confidente.
11. T8 · «Coordinación con realización» (orden de las señas, protocolos de ensayo, quién pide qué en directo): la da RTVE sonido/12 (lenguaje de señas) y realizacion-tv/18; nada normativo añadido. Es costumbre de oficio y así debe decirse.
12. T9 · Formatos de intercambio de sesiones (AAF, OMF, AES31) y entrega en stems: no leídos en esta fase.
13. T9 · Doblaje (más allá del ADR de RTVE produccion/11): sin fuente nueva.

## Reparto para el redactor (qué fuente cubre qué parte del enunciado)

- T4 «niveles»: 4.7 y 4.9 (+ RTVE). «entradas»: 4.1. «salidas»: 4.2. «buses, auxiliares»: 4.3. «grupos»: 4.4. «matrices»: 4.2 y 4.3. «automatización»: 4.8. «escenas»: 4.5. Escucha y órdenes: 4.6.
- T6 «informativos»: 6.1-6.3. «exteriores»: 6.1, 6.4 (+ RTVE ENG). «eventos»: 6.4. «deportes»: 6.5 → 8.2. «musicales»: 8.2 (Show). Ficción y documentales: RTVE.
- T7 «híbridos»: 7.10 (+ RTVE). «RDSI/IP, códecs»: 7.1-7.6. «telefonía»: 7.4 (G.711/G.722) y 7.10. «streaming»: 7.7-7.8. «podcast»: 7.9.
- T8 «intercom»: 8.1 y 8.4. «IFB»: 8.3. «retornos»: RTVE (N-1) + 8.1 («mix-minus») + 4.3 (Mix Minus de consola). «mezcla para emisión»: 8.2. «coordinación con realización»: RTVE + 8.3. «cámaras»: 8.4.
- T9 «cuñas, ráfagas y continuidad»: 9.1 (+ RTVE). «DAW, pistas, sincronía»: RTVE + 9.2. «limpieza»: 9.3. «mezcla y entrega»: 9.2 y 9.4 (+ 8.2).
