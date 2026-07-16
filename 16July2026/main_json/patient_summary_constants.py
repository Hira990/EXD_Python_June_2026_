atherosclerosis_inner_keys = [
    'total', 'lowDensityNonCalcified', 'nonCalcified', 'calcified', 'percentAtheromaVolume'
]

def patient_summary_json():
    return {
        'patient': None,
        'dateOfBirth': None,
        'mrn': None,
        'cleerlyId': None,
        'studyDate': None,
        'provider': None,
        #
        'summary': {
            'atherosclerosis': None,
            'stenosis': None,
            'ischemia': None,
            'dominance': None,
            'exclusions': None
        },
        #
        'atherosclerosis': {
            'rca': {**{k: None for k in atherosclerosis_inner_keys}},
            'lm+lad': {**{k: None for k in atherosclerosis_inner_keys}},
            'cx': {**{k: None for k in atherosclerosis_inner_keys}},
            'total': {**{k: None for k in atherosclerosis_inner_keys}},
        },
        'stenosis': {
            'severe': {'detail': None, 'level': None},
            'moderate': {'detail': None, 'level': None},
            'mild': {'detail': None, 'level': None},
            'minimal': {'detail': None, 'level': None}
        }
    }