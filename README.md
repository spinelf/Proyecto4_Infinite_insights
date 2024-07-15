## Módulo 5: Visualización de datos / Power BI

### Resumen

¡Bienvenid@s al emocionante proyecto "Data Insights: ETL y Visualización Impactante en Power BI"!

![logoINFINITE](https://github.com/RachelCaste/project-da-promo-H-modulo-4-team-2/assets/99440874/d08b8201-38cd-48c1-93f2-b6b64a0f1a52)

_ _ _

### ¿Quiénes Somos?

Desde el año 2001, nuestro equipo de profesionales se ha dedicado a la ciencia de datos, ofreciendo soluciones innovadoras y personalizadas para empresas de diversos sectores. Con más de dos décadas de experiencia, nos enorgullecemos de ser pioneros en el campo de la analítica y la gestión de datos, ayudando a nuestros clientes a transformar sus datos en información valiosa que impulsa decisiones estratégicas y optimiza resultados.

_ _ _

## Proyecto Grupo Molokai


<img width="203" alt="logo - copia" src="https://github.com/RachelCaste/project-da-promo-H-modulo-4-team-2/assets/99440874/6abf7bc0-3d70-41ae-a2bd-281bfcb22700">

### Problema de este conjunto de datos: Análisis y Optimización de Cancelaciones de Reservas

  <p> El hotel ha notado un aumento en el número de cancelaciones de reservas en los últimos meses y necesita comprender las causas y patrones detrás de estas cancelaciones para tomar medidas correctivas. 
  El objetivo es llevar a cabo un análisis exhaustivo de las cancelaciones de reservas y crear visualizaciones impactantes para que la gerencia pueda identificar áreas de mejora y tomar decisiones informadas 
  para reducir la tasa de cancelación. </p>


### Fases del Proyecto 

**Fase 1:** Limpieza de datos

**Fase 2:** Análisis de datos

**Fase 3:** Visualización de datos

**Fase 4:** Cuadros de mandos e historias de datos

**Fase 5:** Conclusiones

<h2> Planificación del proyecto</h2>

      Presentación requerimientos proyecto: 13/06/24
      
      Sprint 1:
       - Duración: 4 sesiones de 2h 
       - Inicio: 14/06/24 (Inclusive)
       - Fin: 19/06/24 (Inclusive)
       - Sprint review: 20/06/24 @11:30h 
 
      Sprint 2:
       - Duración: 5 sesiones de 2h 
       - Inicio: 24/06/24 (Inclusive)
       - Fin: 28/06/24 (Inclusive)
       - Sprint review: 01/07/24 @11:30h

      DEMO / Fin del proyecto: 03/07/24 

</br>
<details>
  <summary> Diccionario de datos proyecto</summary>
  </br>
        <table>
            <thead>
                <tr>
                    <th>Columna</th>
                    <th>Descripción</th>
                </tr>
            </thead>
            <tbody>
                   <tr><td>hotel</td><td> Tipo de hotel</td></tr>
                   <tr><td>is_canceled</td><td> Indica si la reserva fue cancelada (True) o no (False)</td></tr>
                   <tr><td>lead_time</td><td> Número de días entre la fecha de reserva y la fecha de llegada al hotel</td></tr>
                   <tr><td>arrival_date_year</td><td> Año de llegada al hotel</td></tr>
                   <tr><td>arrival_date_month</td><td> Mes de llegada al hotel</td></tr>
                   <tr><td>arrival_date_week_number</td><td> Número de la semana de llegada al hotel</td></tr>
                   <tr><td>arrival_date_day_of_month</td><td> Día del mes de llegada al hotel</td></tr>
                   <tr><td>stays_in_weekend_nights</td><td> Número de noches que el cliente se quedó durante el fin de semana</td></tr>
                   <tr><td>stays_in_week_nights</td><td> Número de noches que el cliente se quedó durante la semana</td></tr>
                   <tr><td>adults</td><td> Número de adultos que acompañaban al cliente en la reserva</td></tr>
                   <tr><td>children</td><td> Número de niños que acompañaban al cliente en la reserva</td></tr>
                   <tr><td>babies</td><td> Número de bebés que acompañaban al cliente en la reserva</td></tr>
                   <tr><td>meal</td><td> Tipo de comida incluida en la reserva (BB: Desayuno, HB: Media Pensión, FB: Pensión Completa)</td></tr>
                   <tr><td>country</td><td> País de origen del cliente</td></tr>
                   <tr><td>market_segment</td><td> Segmento de mercado al que pertenece la reserva</td></tr>
                   <tr><td>distribution_channel</td><td> Canal de distribución utilizado para realizar la reserva</td></tr>
                   <tr><td>is_repeated_guest</td><td> Indica si el cliente es un huésped repetido (1) o no (0)</td></tr>
                   <tr><td>previous_cancellations</td><td> Número de reservas canceladas por el cliente antes de esta reserva</td></tr>
                   <tr><td>previous_bookings_not_canceled</td><td> Número de reservas no canceladas por el cliente antes de esta reserva</td></tr>
                   <tr><td>Freserved_room_type</td><td> Tipo de habitación reservada</td></tr>
                   <tr><td>assigned_room_type</td><td> Tipo de habitación asignada en la reserva</td></tr>
                   <tr><td>booking_changes</td><td> Número de cambios realizados en la reserva</td></tr>
                   <tr><td>agent</td><td> Identificador del agente involucrado en la reserva</td></tr>
                   <tr><td>company</td><td> Identificador de la compañía involucrada en la reserva</td></tr>
                   <tr><td>days_in_waiting_list</td><td> Número de días que la reserva estuvo en lista de espera</td></tr>
                   <tr><td>customer_type</td><td> Tipo de cliente que realizó la reserva (Transient, Contract, Group, Transient-Party)</td></tr>
                   <tr><td>adr</td><td> Tarifa promedio diaria pagada por la reserva</td></tr>
                   <tr><td>required_car_parking_spaces</td><td> Número de espacios de estacionamiento requeridos por el cliente</td></tr>
                   <tr><td>total_of_special_requests</td><td> Número total de solicitudes especiales realizadas por el cliente</td>
                   <tr><td>reservation_status</td><td> Estado de la reserva (Check-Out: Salida, Canceled: Cancelada)</td></tr>
                   <tr><td>reservation_status_date</td><td> Fecha del estado de la reserva</td></tr>
            </tbody>
          </table>
</details>

<details>
  <summary> Intrucciones ejecución</summary>
  </br>
  <p> Para ver la página web del proyecto, nos descargamos el fichero comprimido (Infinite_insights.rar), lo descomprimimos en local. Entrando en la carpeta del proyecto Infinite_insights hacemos doble clic sobre el fichero index.html, a partir de ahi podemos navegar por todas las opciones de la página. </p>
</details>

### Personas del Equipo


* Raquel Castellanos Alfonso (https://www.linkedin.com/in/raquel-castellanos-alfonso)
* Paola Sánchez Solórzano (https://www.linkedin.com/in/paola-sánchez-solórzano-5a05751b4)
* Isabel Martínez Torrego (https://www.linkedin.com/in/isabelmartineztorrego)
* Lidia Fraile Martin
* Silvia Piñel Fañanás (https://www.linkedin.com/in/silviapiñel)



_ _ _

### Herramnientas utilizadas:

    Python
    Visual Studio Code
    Power BI
    Github
    Slack
    Figma
    Canva
    Bootstrap
    HTML5
