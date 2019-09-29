# Question 5

network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
        }},
    'B': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.3,
            (True,): 0.3
        }},

    'C': {
        'Parents': ['A'],
        'CPT': {
            (False,): 0.5,
            (True,): 0.5
        }},
}

# Question 6
network = {
    'A': {
        'Parents': [],
        'CPT': {
            (): 0.1
        }

    },
    'B': {
        'Parents': [],
        'CPT': {
            (): 0.2
        }

    },
    'C': {
        'Parents': [],
        'CPT': {
            (): 0.3
        }

    },
    'D': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.4,
            (False,): 0.5,
        }

    },
    'E': {
        'Parents': ['B'],
        'CPT': {
            (True,): 0.4,
            (False,): 0.5,
        }

    },
}