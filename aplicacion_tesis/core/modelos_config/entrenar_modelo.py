from sklearn.model_selection import RandomizedSearchCV, GridSearchCV
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, make_scorer
from sklearn.exceptions import UndefinedMetricWarning, ConvergenceWarning
import warnings

warnings.filterwarnings("ignore", category=UndefinedMetricWarning)
warnings.filterwarnings("ignore", category=ConvergenceWarning)

# Crear las métricas personalizadas
accuracy_scorer = make_scorer(accuracy_score)
precision_scorer = make_scorer(precision_score, zero_division=0)
recall_scorer = make_scorer(recall_score, zero_division=0)
f1_scorer = make_scorer(f1_score, zero_division=0)

# Para roc_auc, necesitamos manejar excepciones si no hay datos suficientes
def safe_roc_auc(y_true, y_pred):
  try:
    return roc_auc_score(y_true, y_pred)
  except ValueError:
    return -1  # Devuelve un valor arbitrario si no se puede calcular

roc_auc_scorer = make_scorer(safe_roc_auc)

def specificity_score(y_true, y_pred):
  tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
  return tn / (tn + fp) if (tn + fp) > 0 else -1

specificity_scorer = make_scorer(specificity_score)

def busqueda_aleatoria(modelo, param_grid):
  random_search = RandomizedSearchCV(
    estimator=modelo,
    param_distributions=param_grid,
    n_iter=2,
    scoring={
      'accuracy': accuracy_scorer,
      'precision': precision_scorer,
      'recall': recall_scorer,
      'f1': f1_scorer,
      'roc_auc': roc_auc_scorer,
      'specificity': specificity_scorer
    },
    refit='roc_auc',
    cv=5,
    n_jobs=-1,
  )
  return random_search

def busqueda_exhaustiva(modelo, param_grid):
  grid_search = GridSearchCV(
    estimator=modelo,
    param_grid=param_grid,
    scoring={
      'accuracy': accuracy_scorer,
      'precision': precision_scorer,
      'recall': recall_scorer,
      'f1': f1_scorer,
      'roc_auc': roc_auc_scorer,
      'specificity': specificity_scorer
    },
    refit='roc_auc',
    cv=5,
    n_jobs=-1,
  )
  return grid_search
