SELECT address
, entity
FROM (
    values
    (0x0d3250c3d5facb74ac15834096397a3ef790ec99, 'zkSync')
    , (0x2c169dfe5fbba12957bdd0ba47d9cedbfe260ca7, 'StarkNet')
    , (0x6887246668a3b87f54deb3b94ba47a6f63f32985, 'Optimism')
    , (0x5050f69a9786f081509234f1a7f4684b5e5b76c9, 'Base')
    , (0xc1b634853cb333d3ad8663715b08f41a3aec47cc, 'Arbitrum')
    , (0x625726c858dbf78c0125436c943bf4b4be9d9033, 'Zora')
    , (0x889e21d7ba3d6dd62e75d4980a4ad1349c61599d, 'Aevo')
    , (0x41b8cd6791de4d8f9e0eaf7861ac506822adce12, 'Kroma')
    , (0xfa46908b587f9102e81ce6c43b7b41b52881c57f, 'Boba')
    , (0x14e4e97bdc195d399ad8e7fc14451c279fe04c8e, 'Lyra')
    , (0x99199a22125034c808ff20f377d91187e8050f2e, 'Mode')
    , (0x415c8893d514f9bc5211d36eeda4183226b84aa7, 'Blast')
    , (0x6017f75108f251a488b045a7ce2a7c15b179d1f2, 'Fraxtal')
    , (0x99526b0e49a95833e734eb556a6abaffab0ee167, 'PGN')
    ) AS x(address, entity)
