([
    [
        {'count': 1, 'name': 'Turbine (River Valley)', 'category': ['River Valley Buildings - Tier 1', 'Starter Buildings'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Toxin Scrubber (River Valley)', 'category': ['River Valley Buildings - Tier 1', 'Starter Buildings'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Irrigator (River Valley)', 'category': ['River Valley Buildings - Tier 1'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Water Pump (River Valley)', 'category': ['River Valley Buildings - Tier 1'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Calcifier (River Valley)', 'category': ['River Valley Buildings - Tier 1'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Excavator (River Valley)', 'category': ['River Valley Buildings - Tier 1'
            ], 'progression': True
        }
    ],
    [
        {'count': 1, 'name': 'Hydroponium (River Valley)', 'category': ['River Valley Buildings - Tier 2'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Beehive (River Valley)', 'category': ['River Valley Buildings - Tier 2'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Solar Amplifier (River Valley)', 'category': ['River Valley Buildings - Tier 2'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Arboretum (River Valley)', 'category': ['River Valley Buildings - Tier 2'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Research Center (River Valley)', 'category': ['River Valley Buildings - Tier 2'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Cloud Seeder (River Valley)', 'category': ['River Valley Buildings - Tier 2'
            ], 'progression': True
        }
    ],
    [
        {'count': 1, 'name': 'Airship (River Valley)', 'category': ['River Valley Buildings - Tier 3'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Recycling Silo (River Valley)', 'category': ['River Valley Buildings - Tier 3'
            ], 'progression_skip_balancing': True
        },
        {'count': 1, 'name': 'Recycling Drone (River Valley)', 'category': ['River Valley Buildings - Tier 3'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Loading Dock (River Valley)', 'category': ['River Valley Buildings - Tier 3'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Pound Lock (River Valley)', 'category': ['River Valley Buildings - Tier 3'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Sonic Pulse (River Valley)', 'category': ['River Valley Buildings - Tier 3'
            ], 'useful': True
        },
        {'count': 1, 'name': 'Wildlife Bridge (River Valley)', 'category': ['River Valley Buildings - Tier 3'
            ], 'progression': True
        },
        {'count': 1, 'name': 'Animal Observatory (River Valley)', 'category': ['River Valley Buildings - Tier 3'
            ], 'progression': True
        }
    ],
    [
        {'count': 1, 'name': 'Tier 1 Done (River Valley)', 'category': ['River Valley Tiers Done'
            ], 'progression_skip_balancing': True
        },
        {'count': 1, 'name': 'Tier 2 Done (River Valley)', 'category': ['River Valley Tiers Done'
            ], 'progression_skip_balancing': True
        },
        {'count': 1, 'name': 'Tier 3 Done (River Valley)', 'category': ['River Valley Tiers Done'
            ], 'progression_skip_balancing': True
        },
        {'count': 1, 'name': 'Rain (River Valley)', 'category': ['River Valley Climate Goals'
            ], 'useful': True
        }
    ],
    [
        {'count': 1, 'name': 'River Valley Unlock', 'category': ['Region Coordinates'
            ], 'progression': True
        }
    ],
    [
        {'count': 2, 'name': 'Restored Ecosystems', 'category': ['Goal'
            ], 'progression': True
        }
    ]
],
[
    [
        {'name': 'River Valley First Greenery', 'region': 'River Valley - Tier 1', 'category': ['River Valley tier 1 Goal'
            ], 'requires': '|Turbine (River Valley)| AND (|Water Pump (River Valley)| OR (|Toxin Scrubber (River Valley)| AND |Irrigator (River Valley)|)'
        },
        {'name': 'River Valley First River', 'region': 'River Valley - Tier 1', 'category': ['River Valley tier 1 Goal'
            ], 'requires': '|Turbine (River Valley)| AND |Water Pump (River Valley)|'
        },
        {'name': 'River Valley Greenery 25% done', 'region': 'River Valley - Tier 1', 'category': ['River Valley tier 1 Goal'
            ], 'requires': '|Turbine (River Valley)| AND |Toxin Scrubber (River Valley)| AND |Irrigator (River Valley)|'
        },
        {'name': 'River Valley Greenery 50% done', 'region': 'River Valley - Tier 1', 'category': ['River Valley tier 1 Goal'
            ], 'requires': '|Turbine (River Valley)| AND |Toxin Scrubber (River Valley)| AND |Irrigator (River Valley)|'
        },
        {'name': 'River Valley Greenery 75% done', 'region': 'River Valley - Tier 1', 'category': ['River Valley tier 1 Goal'
            ], 'requires': '|Turbine (River Valley)| AND |Toxin Scrubber (River Valley)| AND |Irrigator (River Valley)| AND |Calcifier (River Valley)|'
        },
        {'name': 'River Valley Greenery 100% done', 'region': 'River Valley - Tier 1', 'category': ['River Valley tier 1 Goal'
            ], 'requires': '|Turbine (River Valley)| AND |Toxin Scrubber (River Valley)| AND |Irrigator (River Valley)| AND |Calcifier (River Valley)| AND |Excavator (River Valley)|'
        }
    ],
    [
        {'name': 'River Valley Tier 2 First Wetlands', 'region': 'River Valley - Tier 2', 'category': ['River Valley tier 2 Goals'
            ], 'requires': '|Hydroponium (River Valley)|'
        },
        {'name': 'River Valley Tier 2 Wetlands Goal', 'region': 'River Valley - Tier 2', 'category': ['River Valley tier 2 Goals'
            ], 'requires': '|Hydroponium (River Valley)|'
        },
        {'name': 'River Valley Tier 2 First Fynbos', 'region': 'River Valley - Tier 2', 'category': ['River Valley tier 2 Goals'
            ], 'requires': '|Beehive (River Valley)|'
        },
        {'name': 'River Valley Tier 2 Fynbos Goal', 'region': 'River Valley - Tier 2', 'category': ['River Valley tier 2 Goals'
            ], 'requires': '|Beehive (River Valley)| AND |Solar Amplifier (River Valley)| AND |Arboretum (River Valley)|'
        },
        {'name': 'River Valley Tier 2 First Fire', 'region': 'River Valley - Tier 2', 'category': ['River Valley tier 2 Goals'
            ], 'requires': '|Beehive (River Valley)| AND |Solar Amplifier (River Valley)|'
        },
        {'name': 'River Valley Tier 2 First Forest', 'region': 'River Valley - Tier 2', 'category': ['River Valley tier 2 Goals'
            ], 'requires': '|Beehive (River Valley)| AND |Solar Amplifier (River Valley)| AND |Arboretum (River Valley)|'
        },
        {'name': 'River Valley Tier 2 Forest Goal', 'region': 'River Valley - Tier 2', 'category': ['River Valley tier 2 Goals'
            ], 'requires': '|Beehive (River Valley)| AND |Solar Amplifier (River Valley)| AND |Arboretum (River Valley)|'
        }
    ],
    [
        {'name': 'River Valley Tier 3 First Recycling', 'region': 'River Valley - Tier 3', 'category': ['River Valley tier 3 Goals'
            ], 'requires': '|Airship (River Valley)| AND |Recycling Drone (River Valley)| AND |Loading Dock (River Valley)|'
        },
        {'name': 'River Valley Tier 3 Recycling <5 Buildings Left', 'region': 'River Valley - Tier 3', 'category': ['River Valley tier 3 Goals'
            ], 'requires': '|Airship (River Valley)| AND |Recycling Drone (River Valley)| AND |Loading Dock (River Valley)| AND |Pound Lock (River Valley)|'
        },
        {'name': 'River Valley Tier 3 One Animal Photo', 'region': 'River Valley - Tier 3', 'category': ['River Valley tier 3 Goals'
            ], 'requires': '|Animal Observatory (River Valley)|'
        },
        {'name': 'River Valley Tier 3 All Animal Photos', 'region': 'River Valley - Tier 3', 'category': ['River Valley tier 3 Goals'
            ], 'requires': '|Animal Observatory (River Valley)| AND (|Recycling Silo (River Valley)| OR (|Airship (River Valley)| AND |Recycling Drone (River Valley)| AND |Loading Dock (River Valley)| AND |Pound Lock (River Valley)|)'
        }
    ],
    [
        {'name': 'River Valley Tier 1 Done', 'region': 'River Valley - Tier 1', 'category': ['Tier Clears'
            ], 'requires': '|Turbine (River Valley)| AND |Toxin Scrubber (River Valley)| AND |Irrigator (River Valley)| AND |Calcifier (River Valley)| AND |Excavator (River Valley)|', 'place_item': ['Tier 1 Done (River Valley)'
            ]
        },
        {'name': 'River Valley Tier 2 Done', 'region': 'River Valley - Tier 2', 'category': ['Tier Clears'
            ], 'requires': '', 'place_item': ['Tier 2 Done (River Valley)'
            ]
        },
        {'name': 'River Valley Liftoff', 'region': 'River Valley - Tier 3', 'category': ['Tier Clears'
            ], 'requires': '|Airship (River Valley)| AND |Recycling Drone (River Valley)| AND |Loading Dock (River Valley)| AND |Pound Lock (River Valley)| AND |Animal Observatory (River Valley)|', 'place_item': ['Restored Ecosystems'
            ]
        }
    ],
    [
        {'name': 'Waterlillies blossom', 'region': 'River Valley - Tier 2', 'category': ['Climate Goals'
            ], 'requires': '|Research Center (River Valley)| AND |Cloud Seeder (River Valley)| AND |Tier 2 Done (River Valley)| AND |Recycling Silo (River Valley)|'
        },
        {'name': 'Salmon run', 'region': 'River Valley - Tier 2', 'category': ['Climate Goals'
            ], 'requires': '|Research Center (River Valley)| AND |Cloud Seeder (River Valley)| AND |Tier 2 Done (River Valley)| AND |Recycling Silo (River Valley)|'
        },
        {'name': 'Rains begin', 'region': 'River Valley - Tier 2', 'category': ['Climate Goals'
            ], 'requires': '|Research Center (River Valley)| AND |Cloud Seeder (River Valley)|', 'place_item': ['River Valley Rain'
            ]
        },
        {'name': 'Wildflower Blooms', 'region': 'River Valley - Tier 2', 'category': ['Climate Goals'
            ], 'requires': '|Research Center (River Valley)|'
        },
        {'name': 'Migratory Birds Return', 'region': 'River Valley - Tier 2', 'category': ['Climate Goals'
            ], 'requires': '|Research Center (River Valley)|'
        },
        {'name': 'Ferns on riverbanks', 'region': 'River Valley - Tier 2', 'category': ['Climate Goals'
            ], 'requires': '|Research Center (River Valley)| AND |Cloud Seeder (River Valley)|'
        },
        {'name': 'Fungi in Forests', 'region': 'River Valley - Tier 2', 'category': ['Climate Goals'
            ], 'requires': '|Research Center (River Valley)| AND |Cloud Seeder (River Valley)|'
        }
    ],
    [
        {'name': 'Victory', 'region': 'World Map', 'victory': True, 'category': ['Goal'
            ], 'requires': 'Restored Ecosystems: 2'
        }
    ]
])