# Model ML untuk Memprediksi & Merehabilitasi Cedera

## Repository Outline
```
1. read.md - Gambaran Umum Project
2. notebook.ipynb - Notebook pengolahan data & pembuatan model
3. inference_notebook.ipynb - Notebook pengujian model dengan data inference
4. basketball_injury.csv - dataset
5. basketball_injury.txt - source data
6. basketInjModelV1.pkl - ML model
7. data_inf.csv - dataset inference
8. deployment - folder yg berisi file-file deployment aplikasi di hugging face
```
## Problem Background
```
1. Mengidentifikasi kekambuhan cidera setelah rehabilitasi
2. Investigasi lanjut penanganggan / fisioterapi cidera
```

## Project Output
```
Classification.
Class 0: Tidak ada potensi terjadi kekambuhan cidera
Class 1: Berpontensi terjadi kekambuhan
```
## Data
```
- Sumber data: https://www.kaggle.com/datasets/ziya07/basketball-player-injury-in-sports-rehabilitation
- Informasi tentang pemain basket yg menjalani rehabilitasi akibat cidera
- Deskripsi Fitur:
    > Player_ID: Unique identifier for each player.
    > Age: Age at the time of injury.
    > Height_cm: Player's height in centimeters.
    > Weight_kg: Player's weight in kilograms.
    > Position: Playing position (e.g., Guard, Forward, Center).
    > Injury_Type: Nature of the injury (e.g., Ankle Sprain, ACL Tear).
    > Injury_Severity: Categorized as Mild, Moderate, or Severe.
    > Date_of_Injury: Date on which the injury occurred.
    > knee_angle_deg: Knee angle (degrees) during movement.
    > jump_height_cm: Maximum jump height (centimeters).
    > ankle_flexion_deg: Ankle flexion angle (degrees).
    > speed_m_s: Movement speed (meters/second).
    > reaction_time_ms: Reaction time (milliseconds) during task execution.
    > Agility_Score: A standardized score representing the player’s agility during gameplay or drills.
    > Endurance_sec: The player’s endurance measured in seconds, typically representing sustained physical activity duration under standardized conditions.
    > Rehabilitation_Program: Type of rehabilitation undertaken (e.g., Physiotherapy, Strength Training).
    > Rehabilitation_Time_weeks: Duration of rehabilitation (weeks).
    > Rehabilitation_Efficiency_Score: Efficiency score (range: 0.5–1.0), reflecting rehabilitation quality and performance recovery.
- Target:
    > Injury_Recurrence: Binary indicator of re-injury post-rehabilitation (0: No, 1: Yes).
```
## Method
```
Pembuatan Model ML menggunakan Algoritma Logistic Regression.
Model akan dievaluasi dengan Confusion Metrics 
```
## Stacks
```
1. pandas
2. numpy
3. mathplotlib
4. scipy
5. seaborn
6. scikit-learn
7. joblib
```
## reference
```
1. https://en.wikipedia.org/wiki/Logistic_regression
2. https://www.alodokter.com/serba-serbi-penanganan-cedera-engkel-yang-tepat
3. https://www.rspondokindah.co.id/id/news/intaian-cedera-lutut-bagi-pemain-basket
```
## Url Apps
`https://huggingface.co/spaces/HelasOn7/Basketball_Player_Injury`
---
