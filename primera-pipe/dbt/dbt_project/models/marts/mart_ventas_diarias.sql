select
    fecha_venta,
    count(*)              as num_ventas,
    sum(cantidad)         as unidades_vendidas,
    sum(total)            as ingresos_totales,
    round(avg(total), 2)  as ticket_medio

from {{ ref('stg_ventas') }}
group by fecha_venta
order by fecha_venta
