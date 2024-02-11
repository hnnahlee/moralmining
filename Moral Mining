!pip install -U pip setuptools wheel
!pip install "spacy~=3.0.3"
!python -m spacy download en_core_web_sm
!pip install git+https://github.com/medianeuroscience/emfdscore.git
!pip install -U scikit-learn
template_input = pd.read_csv('sFamily.csv',header=None)
template_input
template_input.to_csv('sFamily.csv', index=False)
%%bash
emfdscore sFamily.csv mfd.csv bow mfd
%%bash
emfdscore sFamily.csv mfd2.csv bow mfd2
template_output = pd.read_csv('sFamily.csv')
template_output
compiled = pd.concat([template_input,template_output], axis = 1)
compiled
