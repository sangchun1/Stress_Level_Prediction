# Stress Level Prediction Project - Setup Guide

이 프로젝트는 스트레스 점수 예측을 위한 머신러닝 모델들을 구현한 프로젝트입니다.

## 📋 Requirements

- Python 3.9+
- Anaconda 또는 Miniconda
- Windows, macOS, 또는 Linux

## 🚀 Quick Setup

### 방법 1: 자동 설치 (권장)

#### Windows
```bash
# 배치 파일 실행
install_requirements.bat
```

#### Linux/macOS
```bash
# 실행 권한 부여
chmod +x install_requirements.sh

# 스크립트 실행
./install_requirements.sh
```

#### Python 스크립트 (모든 플랫폼)
```bash
python setup_environment.py
```

### 방법 2: 수동 설치

1. **Conda 환경 생성**
```bash
conda create -n stress_prediction python=3.9 -y
conda activate stress_prediction
```

2. **필요한 패키지 설치**
```bash
pip install -r requirements.txt
```

3. **성능 향상을 위한 추가 패키지 설치**
```bash
conda install -c conda-forge mkl mkl-include intel-openmp -y
```

4. **Jupyter Kernel 설치**
```bash
python -m ipykernel install --user --name stress_prediction --display-name 'Stress Prediction'
```

## 📦 설치되는 패키지

### Core Data Science Libraries
- `pandas>=1.5.0` - 데이터 조작 및 분석
- `numpy>=1.21.0` - 수치 계산
- `matplotlib>=3.5.0` - 시각화
- `seaborn>=0.11.0` - 통계 시각화

### Machine Learning Libraries
- `scikit-learn>=1.1.0` - 머신러닝 알고리즘
- `lightgbm>=3.3.0` - LightGBM 모델
- `catboost>=1.1.0` - CatBoost 모델
- `xgboost>=1.6.0` - XGBoost 모델

### Jupyter and Development
- `jupyter>=1.0.0` - Jupyter Notebook
- `ipykernel>=6.0.0` - Jupyter Kernel
- `notebook>=6.4.0` - Jupyter Notebook 서버

### Additional Utilities
- `joblib>=1.1.0` - 모델 저장/로드
- `tqdm>=4.64.0` - 진행률 표시
- `numba>=0.56.0` - 성능 최적화

## 🎯 사용법

### 환경 활성화
```bash
conda activate stress_prediction
```

### Jupyter Notebook 시작
```bash
jupyter notebook
```

### Jupyter Lab 시작
```bash
jupyter lab
```

## 📁 프로젝트 구조

```
Stress_Level_Prediction/
├── data/                          # 데이터 파일
│   ├── train.csv                  # 원본 훈련 데이터
│   ├── test.csv                   # 원본 테스트 데이터
│   └── train_preprocessed.csv     # 전처리된 데이터
├── preprocess/                    # 전처리
│   └── preprocess.ipynb          # 데이터 전처리 노트북
├── model/                         # 모델링
│   ├── lightgbm.ipynb            # LightGBM 모델
│   ├── catboost.ipynb            # CatBoost 모델
│   ├── xgboost.ipynb             # XGBoost 모델
│   ├── randomforest.ipynb        # Random Forest 모델
│   └── ensemble.ipynb            # 앙상블 모델
├── requirements.txt               # 필요한 패키지 목록
├── install_requirements.bat       # Windows 설치 스크립트
├── install_requirements.sh        # Linux/macOS 설치 스크립트
├── setup_environment.py          # Python 설치 스크립트
└── README_SETUP.md               # 이 파일
```

## 🔧 노트북 실행 순서

1. **데이터 전처리**
   ```bash
   # preprocess/preprocess.ipynb 실행
   ```

2. **개별 모델 훈련** (순서 무관)
   ```bash
   # model/lightgbm.ipynb
   # model/catboost.ipynb
   # model/xgboost.ipynb
   # model/randomforest.ipynb
   ```

3. **앙상블 모델**
   ```bash
   # model/ensemble.ipynb 실행
   ```

## ⚠️ 주의사항

- 모든 모델은 MAE (Mean Absolute Error)를 메트릭으로 사용합니다
- 하이퍼파라미터 튜닝은 GridSearchCV를 사용합니다
- 모델 파일은 `model/` 디렉토리에 저장됩니다

## 🐛 문제 해결

### Conda 명령어를 찾을 수 없는 경우
```bash
# Anaconda Prompt 사용 또는
# 환경 변수 PATH에 Anaconda 경로 추가
```

### 패키지 설치 실패
```bash
# 캐시 정리 후 재시도
conda clean --all
pip cache purge
```

### Jupyter Kernel 문제
```bash
# Kernel 재설치
conda activate stress_prediction
python -m ipykernel install --user --name stress_prediction --display-name 'Stress Prediction' --force
```

## 📞 지원

문제가 발생하면 다음을 확인해주세요:
1. Python 버전이 3.9 이상인지 확인
2. Conda가 올바르게 설치되어 있는지 확인
3. 인터넷 연결 상태 확인
4. 방화벽이나 프록시 설정 확인 