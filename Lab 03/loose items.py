ones = 0
    oneties = 0
    hundreds = 0
    thousands = 0
    millions = 0
    billions = 0
    trillions = 0
    quadrillions = 0
    quintillions = 0
    sextillions = 0
    oneties, below_tens = divmod(number, 10)
    if oneties > 10:
        hundreds, tens = divmod(oneties, 10)

    if hundreds > 10:
        thousands, hundreds = divmod(hundreds, 10)

    if thousands > 10:
        millions, thousands = divmod(thousands, 10)

    if millions > 10:
        billions, millions = divmod(millions, 10)

    if billions > 10:
        trillions, billions = divmod(billions, 10)

    if trillions> 10:
        quadrillions, trillions = divmod(trillions, 10)

    if quadrillions > 10:
        quintillions, quadrillions = divmod(quadrillions, 10)

    if quintillions > 10:
        sextillions, quintillions = divmod(quintillions, 10)

