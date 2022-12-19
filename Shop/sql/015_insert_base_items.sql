INSERT INTO
    IS601_Products (
        id,
        name,
        description,
        category,
        stock,
        unit_price,
        image,
        visibility
    )
VALUES (
        -1,
        "Health Boost",
        "Live longer",
        "XYZ",
        9999999,
        10,
        "",
        false
    ), (
        -2,
        "Agility",
        "Become the flash",
        "XYZ",
        9999999,
        15,
        "",
        true
    ), (
        -3,
        "Quick Shot",
        "More pew pew",
        "XYZ",
        9999999,
        5,
        "",
        true
    ), (
        -4,
        "Large Caliber",
        "One shot wonder",
        "XYZ",
        9999999,
        20,
        "",
        true
    ), (
        -5,
        "Vaccuum",
        "Channel your inner Kirby",
        "XYZ",
        9999999,
        1,
        "",
        true
    ) ON DUPLICATE KEY
UPDATE
    modified = CURRENT_TIMESTAMP()