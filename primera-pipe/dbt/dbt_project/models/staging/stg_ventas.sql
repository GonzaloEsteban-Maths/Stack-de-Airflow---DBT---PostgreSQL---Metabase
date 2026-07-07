with fuente as (

    select *
    from {{ source('raw', 'ventas') }}

),

renombrado as (

    select
        id                          as venta_id,
        uuid                        as venta_uuid,
        trim(cliente)               as cliente,
        lower(trim(email))          as email,
        producto,
        categoria,
        cantidad,
        precio_unit,
        total,
        pais,
        creado_en,
        ingerido_en,
        date_trunc('day', creado_en) as fecha_venta

    from fuente

)

select *
from renombrado
