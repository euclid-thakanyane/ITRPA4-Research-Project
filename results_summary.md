# ITRPA4 Mini Dissertation: Results Summary

*This file is generated automatically by `itrpa_experiments.ipynb`. Every number below comes from that notebook run (SEED = 42).*

## 1. Dataset

|                   |      value |
|:------------------|-----------:|
| n_states          |    48.0000 |
| n_keywords        |   525.0000 |
| n_features        |   545.0000 |
| n_aux             |    20.0000 |
| n_train           | 52560.0000 |
| n_test            | 23280.0000 |
| steps_train       |  1095.0000 |
| steps_test        |   485.0000 |
| aux_monotone_frac |     1.0000 |
| label_runs        |   198.0000 |
| label_runs_div7   |     0.7879 |

### 1.1 Sparsity

|                             |     value |
|:----------------------------|----------:|
| density_train               |    0.0705 |
| density_test                |    0.0556 |
| density_all                 |    0.0659 |
| density_keywords_only_all   |    0.0427 |
| density_aux_only_all        |    0.6735 |
| sparsity_train              |    0.9295 |
| sparsity_test               |    0.9444 |
| sparsity_all                |    0.9341 |
| sparsity_keywords_only_all  |    0.9573 |
| sparsity_aux_only_all       |    0.3265 |
| feature_zero_rate_median    |    0.9705 |
| feature_zero_rate_mean      |    0.9295 |
| n_features_nonzero_lt_1pct  |   43.0000 |
| n_features_nonzero_lt_5pct  |  370.0000 |
| n_features_nonzero_ge_50pct |   20.0000 |
| obs_zero_rate_median        |    0.9431 |
| obs_zero_rate_mean          |    0.9295 |
| n_obs_all_zero_train        | 2904.0000 |
| n_obs_all_zero_test         | 2073.0000 |
| max_count_train             | 1112.0000 |

### 1.2 Top 20 keywords by total training count

| feature   |   total_count_train |   nonzero_rate_train |   zero_rate_train |
|:----------|--------------------:|---------------------:|------------------:|
| flu       |         849856.0000 |               0.8928 |            0.1072 |
| sick      |          71736.0000 |               0.4673 |            0.5327 |
| stomach   |          66786.0000 |               0.4498 |            0.5502 |
| cold      |          51720.0000 |               0.4216 |            0.5784 |
| week      |          26230.0000 |               0.2651 |            0.7349 |
| swine     |          22538.0000 |               0.2648 |            0.7352 |
| work      |          21655.0000 |               0.2460 |            0.7540 |
| days      |          20409.0000 |               0.2286 |            0.7714 |
| feeling   |          20118.0000 |               0.2387 |            0.7613 |
| home      |          19793.0000 |               0.2191 |            0.7809 |
| around    |          19271.0000 |               0.2070 |            0.7930 |
| season    |          19085.0000 |               0.1919 |            0.8081 |
| bed       |          18367.0000 |               0.2189 |            0.7811 |
| symptoms  |          18311.0000 |               0.2114 |            0.7886 |
| away      |          16217.0000 |               0.1935 |            0.8065 |
| year      |          13552.0000 |               0.1583 |            0.8417 |
| fever     |          13225.0000 |               0.1669 |            0.8331 |
| sucks     |          12992.0000 |               0.1652 |            0.8348 |
| tomorrow  |          12941.0000 |               0.1700 |            0.8300 |
| tonight   |          12837.0000 |               0.1555 |            0.8445 |

### 1.3 Class imbalance by split

|       |          n |   positives |   negatives |   prevalence |   imbalance_ratio |
|:------|-----------:|------------:|------------:|-------------:|------------------:|
| train | 52560.0000 |   2905.0000 |  49655.0000 |       0.0553 |           17.0929 |
| test  | 23280.0000 |   2282.0000 |  20998.0000 |       0.0980 |            9.2016 |
| all   | 75840.0000 |   5187.0000 |  70653.0000 |       0.0684 |           13.6212 |

### 1.4 Class imbalance by state

| state                |   train_prevalence |   test_prevalence |   train_pos |   test_pos |   train_IR |   test_IR |
|:---------------------|-------------------:|------------------:|------------:|-----------:|-----------:|----------:|
| alabama              |             0.2265 |            0.2804 |    248.0000 |   136.0000 |     3.4153 |    2.5662 |
| texas                |             0.1562 |            0.2948 |    171.0000 |   143.0000 |     5.4035 |    2.3916 |
| louisiana            |             0.1498 |            0.2371 |    164.0000 |   115.0000 |     5.6768 |    3.2174 |
| mississippi          |             0.1434 |            0.2804 |    157.0000 |   136.0000 |     5.9745 |    2.5662 |
| oklahoma             |             0.1242 |            0.2948 |    136.0000 |   143.0000 |     7.0515 |    2.3916 |
| arkansas             |             0.1050 |            0.2515 |    115.0000 |   122.0000 |     8.5217 |    2.9754 |
| missouri             |             0.1050 |            0.1072 |    115.0000 |    52.0000 |     8.5217 |    8.3269 |
| virginia             |             0.0986 |            0.1794 |    108.0000 |    87.0000 |     9.1389 |    4.5747 |
| new jersey           |             0.0959 |            0.0433 |    105.0000 |    21.0000 |     9.4286 |   22.0952 |
| indiana              |             0.0895 |            0.0577 |     98.0000 |    28.0000 |    10.1735 |   16.3214 |
| north carolina       |             0.0795 |            0.0928 |     87.0000 |    45.0000 |    11.5862 |    9.7778 |
| illinois             |             0.0795 |            0.0784 |     87.0000 |    38.0000 |    11.5862 |   11.7632 |
| tennessee            |             0.0795 |            0.1505 |     87.0000 |    73.0000 |    11.5862 |    5.6438 |
| south carolina       |             0.0731 |            0.0639 |     80.0000 |    31.0000 |    12.6875 |   14.6452 |
| georgia              |             0.0703 |            0.0722 |     77.0000 |    35.0000 |    13.2208 |   12.8571 |
| utah                 |             0.0703 |            0.0866 |     77.0000 |    42.0000 |    13.2208 |   10.5476 |
| nebraska             |             0.0703 |            0.0433 |     77.0000 |    21.0000 |    13.2208 |   22.0952 |
| kansas               |             0.0667 |            0.2660 |     73.0000 |   129.0000 |    14.0000 |    2.7597 |
| new mexico           |             0.0667 |            0.0784 |     73.0000 |    38.0000 |    14.0000 |   11.7632 |
| district of columbia |             0.0539 |            0.0928 |     59.0000 |    45.0000 |    17.5593 |    9.7778 |
| west virginia        |             0.0511 |            0.1443 |     56.0000 |    70.0000 |    18.5536 |    5.9286 |
| colorado             |             0.0475 |            0.1072 |     52.0000 |    52.0000 |    20.0577 |    8.3269 |
| wyoming              |             0.0447 |            0.0433 |     49.0000 |    21.0000 |    21.3469 |   22.0952 |
| vermont              |             0.0447 |            0.1010 |     49.0000 |    49.0000 |    21.3469 |    8.8980 |
| idaho                |             0.0411 |            0.1361 |     45.0000 |    66.0000 |    23.3333 |    6.3485 |
| nevada               |             0.0411 |            0.1072 |     45.0000 |    52.0000 |    23.3333 |    8.3269 |
| delaware             |             0.0384 |            0.0289 |     42.0000 |    14.0000 |    25.0714 |   33.6429 |
| michigan             |             0.0320 |            0.0144 |     35.0000 |     7.0000 |    30.2857 |   68.2857 |
| maryland             |             0.0256 |            0.0289 |     28.0000 |    14.0000 |    38.1071 |   33.6429 |
| north dakota         |             0.0256 |            0.0144 |     28.0000 |     7.0000 |    38.1071 |   68.2857 |
| california           |             0.0219 |            0.0639 |     24.0000 |    31.0000 |    44.6250 |   14.6452 |
| alaska               |             0.0219 |            0.0206 |     24.0000 |    10.0000 |    44.6250 |   47.5000 |
| oregon               |             0.0219 |            0.0206 |     24.0000 |    10.0000 |    44.6250 |   47.5000 |
| rhode island         |             0.0192 |            0.0433 |     21.0000 |    21.0000 |    51.1429 |   22.0952 |
| hawaii               |             0.0192 |            0.1299 |     21.0000 |    63.0000 |    51.1429 |    6.6984 |
| connecticut          |             0.0192 |            0.0866 |     21.0000 |    42.0000 |    51.1429 |   10.5476 |
| arizona              |             0.0192 |            0.0289 |     21.0000 |    14.0000 |    51.1429 |   33.6429 |
| ohio                 |             0.0192 |            0.0289 |     21.0000 |    14.0000 |    51.1429 |   33.6429 |
| minnesota            |             0.0192 |            0.1155 |     21.0000 |    56.0000 |    51.1429 |    7.6607 |
| pennsylvania         |             0.0128 |            0.1155 |     14.0000 |    56.0000 |    77.2143 |    7.6607 |
| washington           |             0.0128 |            0.0577 |     14.0000 |    28.0000 |    77.2143 |   16.3214 |
| new york             |             0.0128 |            0.1155 |     14.0000 |    56.0000 |    77.2143 |    7.6607 |
| iowa                 |             0.0064 |            0.0144 |      7.0000 |     7.0000 |   155.4286 |   68.2857 |
| florida              |             0.0064 |            0.0289 |      7.0000 |    14.0000 |   155.4286 |   33.6429 |
| new hampshire        |             0.0064 |            0.0000 |      7.0000 |     0.0000 |   155.4286 |  nan      |
| massachusetts        |             0.0064 |            0.0144 |      7.0000 |     7.0000 |   155.4286 |   68.2857 |
| maine                |             0.0064 |            0.0000 |      7.0000 |     0.0000 |   155.4286 |  nan      |
| wisconsin            |             0.0064 |            0.0433 |      7.0000 |    21.0000 |   155.4286 |   22.0952 |

## 2. Preprocessing comparison (LogReg-L2, 5-fold stratified CV on train)

| preprocessing   |   cv_pr_auc |   cv_roc_auc |
|:----------------|------------:|-------------:|
| log1p + MaxAbs  |      0.3530 |       0.8195 |
| minmax (MaxAbs) |      0.3311 |       0.8041 |
| TF-IDF          |      0.3053 |       0.8176 |

Selected: **log1p + MaxAbs**


## 3. Hyperparameter tuning (5-fold stratified CV PR-AUC on train)

|                         | best_params                                                                               |   cv_pr_auc |   oof_pr_auc |
|:------------------------|:------------------------------------------------------------------------------------------|------------:|-------------:|
| LogReg-L1               | {'clf__C': 0.1}                                                                           |      0.3704 |       0.3700 |
| LogReg-L2               | {'clf__C': 0.1}                                                                           |      0.3661 |       0.3650 |
| Poisson-count           | n/a                                                                                       |    nan      |       0.3492 |
| NegBin-count            | n/a                                                                                       |    nan      |       0.3995 |
| Bayesian-LR (horseshoe) | PyMC 6.4.0 horseshoe prior, mean-field ADVI (30k iters, 1000 draws), top-50 chi2 features |    nan      |     nan      |
| RandomForest            | {'max_depth': None, 'min_samples_leaf': 5}                                                |      0.3338 |       0.3326 |
| XGBoost                 | {'learning_rate': 0.05, 'max_depth': 4, 'n_estimators': 400}                              |      0.3723 |       0.3711 |
| LightGBM                | {'learning_rate': 0.05, 'n_estimators': 400, 'num_leaves': 15}                            |      0.3850 |       0.3843 |
| MLP                     | {'clf__alpha': 0.001}                                                                     |      0.2046 |       0.2036 |

## 4. Test-set results (provided test split)

|                         | family      |   pr_auc |   roc_auc |     f1 |   precision |   recall |    mcc |   balanced_acc |   accuracy |   brier |   threshold |
|:------------------------|:------------|---------:|----------:|-------:|------------:|---------:|-------:|---------------:|-----------:|--------:|------------:|
| LightGBM                | ML          |   0.3823 |    0.7887 | 0.3956 |      0.4374 |   0.3611 | 0.3386 |         0.6553 |     0.8918 |  0.1350 |      0.7007 |
| XGBoost                 | ML          |   0.3809 |    0.7827 | 0.3713 |      0.4808 |   0.3024 | 0.3300 |         0.6334 |     0.8996 |  0.1362 |      0.7282 |
| LogReg-L1               | Statistical |   0.3761 |    0.7947 | 0.3639 |      0.4661 |   0.2984 | 0.3203 |         0.6306 |     0.8977 |  0.1530 |      0.7856 |
| LogReg-L2               | Statistical |   0.3708 |    0.7929 | 0.3828 |      0.4215 |   0.3506 | 0.3241 |         0.6491 |     0.8892 |  0.1544 |      0.7381 |
| RandomForest            | ML          |   0.3340 |    0.7433 | 0.3176 |      0.4672 |   0.2406 | 0.2863 |         0.6054 |     0.8987 |  0.0893 |      0.3986 |
| NegBin-count            | Statistical |   0.3076 |    0.7926 | 0.2139 |      0.4377 |   0.1415 | 0.2067 |         0.5609 |     0.8980 |  0.0871 |      0.1492 |
| Bayesian-LR (horseshoe) | Statistical |   0.2994 |    0.7477 | 0.2904 |      0.4158 |   0.2230 | 0.2518 |         0.5945 |     0.8931 |  0.0839 |      0.1207 |
| Poisson-count           | Statistical |   0.2716 |    0.7027 | 0.2301 |      0.5105 |   0.1486 | 0.2377 |         0.5665 |     0.9026 |  0.1003 |      1.0000 |
| MLP                     | ML          |   0.1855 |    0.5368 | 0.2169 |      0.4415 |   0.1437 | 0.2097 |         0.5620 |     0.8982 |  0.1061 |      0.8465 |

### 4.1 Best model per metric (test)

|              | best model              |
|:-------------|:------------------------|
| pr_auc       | LightGBM                |
| roc_auc      | LogReg-L1               |
| f1           | LightGBM                |
| precision    | Poisson-count           |
| recall       | LightGBM                |
| mcc          | LightGBM                |
| balanced_acc | LightGBM                |
| brier        | Bayesian-LR (horseshoe) |

Best statistical model (PR-AUC): **LogReg-L1**; best ML model (PR-AUC): **LightGBM**


### 4.2 Count-model coefficients

|               |   outbreak_log_rate_ratio |   rate_ratio |   nb_alpha |
|:--------------|--------------------------:|-------------:|-----------:|
| Poisson-count |                    1.3278 |       3.7728 |   nan      |
| NegBin-count  |                    1.2628 |       3.5355 |     0.6168 |

### 4.3 Bayesian LR

Method: PyMC 6.4.0 horseshoe prior, mean-field ADVI (30k iters, 1000 draws), top-50 chi2 features


|                     |   value |
|:--------------------|--------:|
| mean_95ci_width     |  0.0355 |
| mean_95ci_width_pos |  0.0844 |
| mean_95ci_width_neg |  0.0302 |

### 4.4 Per-state test PR-AUC

| state                |   positives |   LogReg-L1 |   LightGBM |
|:---------------------|------------:|------------:|-----------:|
| texas                |         143 |      0.8804 |     0.8810 |
| alabama              |         136 |      0.8088 |     0.8379 |
| arkansas             |         122 |      0.8256 |     0.8132 |
| oklahoma             |         143 |      0.8076 |     0.7947 |
| louisiana            |         115 |      0.7817 |     0.7862 |
| virginia             |          87 |      0.7088 |     0.7445 |
| kansas               |         129 |      0.7368 |     0.7001 |
| tennessee            |          73 |      0.6945 |     0.6752 |
| north carolina       |          45 |      0.6140 |     0.6217 |
| south carolina       |          31 |      0.5468 |     0.5924 |
| minnesota            |          56 |      0.5664 |     0.5806 |
| michigan             |           7 |      0.5268 |     0.5290 |
| illinois             |          38 |      0.5638 |     0.5060 |
| mississippi          |         136 |      0.5957 |     0.4926 |
| georgia              |          35 |      0.3807 |     0.4841 |
| ohio                 |          14 |      0.5652 |     0.4783 |
| pennsylvania         |          56 |      0.4301 |     0.4694 |
| indiana              |          28 |      0.3712 |     0.4640 |
| new york             |          56 |      0.4154 |     0.4082 |
| missouri             |          52 |      0.4012 |     0.3549 |
| maryland             |          14 |      0.3751 |     0.3496 |
| west virginia        |          70 |      0.3602 |     0.3437 |
| colorado             |          52 |      0.2909 |     0.3120 |
| oregon               |          10 |      0.1643 |     0.2645 |
| utah                 |          42 |      0.2804 |     0.2475 |
| district of columbia |          45 |      0.2247 |     0.2397 |
| idaho                |          66 |      0.2692 |     0.2358 |
| nevada               |          52 |      0.2623 |     0.2308 |
| washington           |          28 |      0.2182 |     0.2295 |
| california           |          31 |      0.3392 |     0.2169 |
| new jersey           |          21 |      0.2779 |     0.2086 |
| hawaii               |          63 |      0.2182 |     0.2070 |
| new mexico           |          38 |      0.2152 |     0.1883 |
| connecticut          |          42 |      0.1684 |     0.1843 |
| wisconsin            |          21 |      0.1207 |     0.1790 |
| vermont              |          49 |      0.1730 |     0.1507 |
| alaska               |          10 |      0.2180 |     0.1462 |
| iowa                 |           7 |      0.1774 |     0.1301 |
| nebraska             |          21 |      0.1543 |     0.1157 |
| rhode island         |          21 |      0.1043 |     0.0989 |
| arizona              |          14 |      0.1246 |     0.0978 |
| florida              |          14 |      0.0593 |     0.0672 |
| massachusetts        |           7 |      0.0480 |     0.0635 |
| wyoming              |          21 |      0.0972 |     0.0473 |
| delaware             |          14 |      0.0420 |     0.0373 |
| north dakota         |           7 |      0.0473 |     0.0366 |

## 5. Dimensionality reduction (RQ3)

| model     | dim_reduction            | imbalance     |   n_features |   cv_pr_auc |   test_pr_auc |   test_roc_auc |   test_f1 |   test_recall |   test_precision |   test_brier |   seconds |
|:----------|:-------------------------|:--------------|-------------:|------------:|--------------:|---------------:|----------:|--------------:|-----------------:|-------------:|----------:|
| LogReg-L2 | All features             | class weights |          545 |      0.3650 |        0.3708 |         0.7929 |    0.3828 |        0.3506 |           0.4215 |       0.1544 |    0.7756 |
| LogReg-L2 | TruncatedSVD (300 comp.) | class weights |          300 |      0.3631 |        0.3746 |         0.7914 |    0.3614 |        0.2932 |           0.4711 |       0.1569 |   16.6357 |
| LogReg-L2 | chi2 top-100             | class weights |          100 |      0.3151 |        0.3451 |         0.7625 |    0.3498 |        0.2875 |           0.4466 |       0.1555 |    0.6227 |
| LogReg-L2 | L1 selection             | class weights |          404 |      0.3646 |        0.3696 |         0.7928 |    0.3474 |        0.2800 |           0.4574 |       0.1544 |   14.2199 |
| LightGBM  | All features             | class weights |          545 |      0.3843 |        0.3823 |         0.7887 |    0.3956 |        0.3611 |           0.4374 |       0.1350 |    4.8509 |
| LightGBM  | TruncatedSVD (300 comp.) | class weights |          300 |      0.3626 |        0.3582 |         0.7579 |    0.3671 |        0.3199 |           0.4307 |       0.1168 |   33.8484 |
| LightGBM  | chi2 top-100             | class weights |          100 |      0.3547 |        0.3541 |         0.7496 |    0.3348 |        0.2568 |           0.4807 |       0.1319 |    3.5418 |
| LightGBM  | L1 selection             | class weights |          404 |      0.3799 |        0.3801 |         0.7880 |    0.3939 |        0.3501 |           0.4501 |       0.1352 |   36.5411 |

## 6. Imbalance handling (RQ3)

| model     | dim_reduction   | imbalance             |   n_features |   cv_pr_auc |   test_pr_auc |   test_roc_auc |   test_f1 |   test_recall |   test_precision |   test_brier |   seconds |
|:----------|:----------------|:----------------------|-------------:|------------:|--------------:|---------------:|----------:|--------------:|-----------------:|-------------:|----------:|
| LogReg-L2 | All features    | none (threshold only) |          545 |      0.3722 |        0.3753 |         0.7894 |    0.3583 |        0.2897 |           0.4695 |       0.0780 |    0.7180 |
| LogReg-L2 | All features    | class weights         |          545 |      0.3650 |        0.3708 |         0.7929 |    0.3828 |        0.3506 |           0.4215 |       0.1544 |    0.7348 |
| LogReg-L2 | All features    | SMOTE                 |          545 |      0.3351 |        0.3409 |         0.7495 |    0.3349 |        0.2708 |           0.4386 |       0.1810 |    2.6504 |
| LogReg-L2 | All features    | random oversampling   |          545 |      0.3600 |        0.3677 |         0.7916 |    0.3665 |        0.3168 |           0.4348 |       0.1543 |    1.9394 |
| LightGBM  | All features    | none (threshold only) |          545 |      0.3877 |        0.3819 |         0.7900 |    0.3631 |        0.2936 |           0.4759 |       0.0770 |    4.9366 |
| LightGBM  | All features    | class weights         |          545 |      0.3843 |        0.3823 |         0.7887 |    0.3956 |        0.3611 |           0.4374 |       0.1350 |    8.1370 |
| LightGBM  | All features    | SMOTE                 |          545 |      0.3219 |        0.2778 |         0.6760 |    0.3251 |        0.2472 |           0.4747 |       0.0820 |   36.1102 |
| LightGBM  | All features    | random oversampling   |          545 |      0.3822 |        0.3781 |         0.7876 |    0.3843 |        0.3374 |           0.4464 |       0.1332 |    9.2088 |

## 7. Sparsity experiments (RQ1)

| experiment   |    value |   n_features | model     |   test_pr_auc |   test_roc_auc |   density |
|:-------------|---------:|-------------:|:----------|--------------:|---------------:|----------:|
| min_df       |   0.0000 |          545 | LogReg-L2 |        0.3708 |         0.7929 |  nan      |
| min_df       |   0.0000 |          545 | LightGBM  |        0.3823 |         0.7887 |  nan      |
| min_df       |   0.0010 |          545 | LogReg-L2 |        0.3708 |         0.7929 |  nan      |
| min_df       |   0.0010 |          545 | LightGBM  |        0.3823 |         0.7887 |  nan      |
| min_df       |   0.0100 |          502 | LogReg-L2 |        0.3720 |         0.7931 |  nan      |
| min_df       |   0.0100 |          502 | LightGBM  |        0.3771 |         0.7874 |  nan      |
| min_df       |   0.0500 |          175 | LogReg-L2 |        0.3670 |         0.7876 |  nan      |
| min_df       |   0.0500 |          175 | LightGBM  |        0.3685 |         0.7749 |  nan      |
| min_df       |   0.1000 |           64 | LogReg-L2 |        0.3389 |         0.7723 |  nan      |
| min_df       |   0.1000 |           64 | LightGBM  |        0.3394 |         0.7540 |  nan      |
| min_df       |   0.2000 |           33 | LogReg-L2 |        0.3132 |         0.7617 |  nan      |
| min_df       |   0.2000 |           33 | LightGBM  |        0.3223 |         0.7450 |  nan      |
| min_df       |   0.3000 |           24 | LogReg-L2 |        0.2928 |         0.7469 |  nan      |
| min_df       |   0.3000 |           24 | LightGBM  |        0.3110 |         0.7295 |  nan      |
| min_df       |   0.5000 |           20 | LogReg-L2 |        0.2885 |         0.7479 |  nan      |
| min_df       |   0.5000 |           20 | LightGBM  |        0.2951 |         0.7310 |  nan      |
| top_k_chi2   |   5.0000 |            5 | LogReg-L2 |        0.2291 |         0.6950 |  nan      |
| top_k_chi2   |   5.0000 |            5 | LightGBM  |        0.2139 |         0.6864 |  nan      |
| top_k_chi2   |  10.0000 |           10 | LogReg-L2 |        0.2540 |         0.7211 |  nan      |
| top_k_chi2   |  10.0000 |           10 | LightGBM  |        0.2417 |         0.7098 |  nan      |
| top_k_chi2   |  25.0000 |           25 | LogReg-L2 |        0.2756 |         0.7372 |  nan      |
| top_k_chi2   |  25.0000 |           25 | LightGBM  |        0.2970 |         0.7212 |  nan      |
| top_k_chi2   |  50.0000 |           50 | LogReg-L2 |        0.3127 |         0.7546 |  nan      |
| top_k_chi2   |  50.0000 |           50 | LightGBM  |        0.3201 |         0.7384 |  nan      |
| top_k_chi2   | 100.0000 |          100 | LogReg-L2 |        0.3451 |         0.7625 |  nan      |
| top_k_chi2   | 100.0000 |          100 | LightGBM  |        0.3541 |         0.7496 |  nan      |
| top_k_chi2   | 200.0000 |          200 | LogReg-L2 |        0.3572 |         0.7674 |  nan      |
| top_k_chi2   | 200.0000 |          200 | LightGBM  |        0.3591 |         0.7549 |  nan      |
| top_k_chi2   | 300.0000 |          300 | LogReg-L2 |        0.3573 |         0.7727 |  nan      |
| top_k_chi2   | 300.0000 |          300 | LightGBM  |        0.3603 |         0.7571 |  nan      |
| top_k_chi2   | 545.0000 |          545 | LogReg-L2 |        0.3708 |         0.7929 |  nan      |
| top_k_chi2   | 545.0000 |          545 | LightGBM  |        0.3823 |         0.7887 |  nan      |
| sparsify     |   0.0000 |          545 | LogReg-L2 |        0.3708 |         0.7929 |    0.0705 |
| sparsify     |   0.0000 |          545 | LightGBM  |        0.3823 |         0.7887 |    0.0705 |
| sparsify     |   0.2500 |          545 | LogReg-L2 |        0.3190 |         0.7669 |    0.0528 |
| sparsify     |   0.2500 |          545 | LightGBM  |        0.3345 |         0.7743 |    0.0528 |
| sparsify     |   0.5000 |          545 | LogReg-L2 |        0.2915 |         0.7468 |    0.0352 |
| sparsify     |   0.5000 |          545 | LightGBM  |        0.3029 |         0.7561 |    0.0352 |
| sparsify     |   0.7500 |          545 | LogReg-L2 |        0.2528 |         0.7201 |    0.0176 |
| sparsify     |   0.7500 |          545 | LightGBM  |        0.2581 |         0.7188 |    0.0176 |
| sparsify     |   0.9000 |          545 | LogReg-L2 |        0.2131 |         0.6936 |    0.0070 |
| sparsify     |   0.9000 |          545 | LightGBM  |        0.2133 |         0.6845 |    0.0070 |
| sparsify     |   0.9500 |          545 | LogReg-L2 |        0.1935 |         0.6641 |    0.0035 |
| sparsify     |   0.9500 |          545 | LightGBM  |        0.1862 |         0.6486 |    0.0035 |

### 7.1 Keywords-only sensitivity

| model     | features          |   test_pr_auc |   test_roc_auc |
|:----------|:------------------|--------------:|---------------:|
| LogReg-L2 | 525 keywords only |        0.3393 |         0.7799 |
| LogReg-L2 | all 545           |        0.3708 |         0.7929 |
| LightGBM  | 525 keywords only |        0.3396 |         0.7725 |
| LightGBM  | all 545           |        0.3823 |         0.7887 |

## 8. Temporal validation

| model         |   temporal_cv_pr_auc_mean |   temporal_cv_pr_auc_std |   temporal_cv_roc_auc_mean |   folds_used |   stratified_cv_pr_auc_oof |   test_pr_auc |
|:--------------|--------------------------:|-------------------------:|---------------------------:|-------------:|---------------------------:|--------------:|
| LightGBM      |                    0.1628 |                   0.1119 |                     0.6968 |       4.0000 |                     0.3843 |        0.3823 |
| XGBoost       |                    0.1614 |                   0.0972 |                     0.6853 |       4.0000 |                     0.3711 |        0.3809 |
| LogReg-L1     |                    0.2004 |                   0.1663 |                     0.7655 |       4.0000 |                     0.3700 |        0.3761 |
| LogReg-L2     |                    0.1900 |                   0.1611 |                     0.7424 |       4.0000 |                     0.3650 |        0.3708 |
| RandomForest  |                    0.1223 |                   0.0999 |                     0.7011 |       4.0000 |                     0.3326 |        0.3340 |
| NegBin-count  |                    0.2330 |                   0.2265 |                     0.8794 |       4.0000 |                     0.3995 |        0.3076 |
| Poisson-count |                    0.1906 |                   0.1800 |                     0.8709 |       4.0000 |                     0.3492 |        0.2716 |
| MLP           |                    0.0946 |                   0.0863 |                     0.5038 |       4.0000 |                     0.2036 |        0.1855 |

Folds:

| model         |   fold |   pr_auc |   roc_auc |   val_prevalence |
|:--------------|-------:|---------:|----------:|-----------------:|
| LightGBM      |      1 |   0.0399 |    0.6564 |           0.0128 |
| LightGBM      |      2 |   0.0965 |    0.7285 |           0.0011 |
| LightGBM      |      3 |   0.2487 |    0.6077 |           0.1492 |
| LightGBM      |      4 |   0.2659 |    0.7944 |           0.0393 |
| XGBoost       |      1 |   0.0499 |    0.6728 |           0.0128 |
| XGBoost       |      2 |   0.1109 |    0.7169 |           0.0011 |
| XGBoost       |      3 |   0.2312 |    0.5640 |           0.1492 |
| XGBoost       |      4 |   0.2537 |    0.7872 |           0.0393 |
| LogReg-L1     |      1 |   0.0627 |    0.7209 |           0.0128 |
| LogReg-L1     |      2 |   0.0650 |    0.7964 |           0.0011 |
| LogReg-L1     |      3 |   0.4016 |    0.7350 |           0.1492 |
| LogReg-L1     |      4 |   0.2721 |    0.8098 |           0.0393 |
| LogReg-L2     |      1 |   0.0521 |    0.6720 |           0.0128 |
| LogReg-L2     |      2 |   0.0582 |    0.7761 |           0.0011 |
| LogReg-L2     |      3 |   0.3757 |    0.7103 |           0.1492 |
| LogReg-L2     |      4 |   0.2737 |    0.8111 |           0.0393 |
| RandomForest  |      1 |   0.0408 |    0.7240 |           0.0128 |
| RandomForest  |      2 |   0.0310 |    0.7763 |           0.0011 |
| RandomForest  |      3 |   0.2044 |    0.5865 |           0.1492 |
| RandomForest  |      4 |   0.2130 |    0.7176 |           0.0393 |
| MLP           |      1 |   0.0168 |    0.4422 |           0.0128 |
| MLP           |      2 |   0.0290 |    0.4517 |           0.0011 |
| MLP           |      3 |   0.1957 |    0.4948 |           0.1492 |
| MLP           |      4 |   0.1370 |    0.6265 |           0.0393 |
| Poisson-count |      1 |   0.0649 |    0.8537 |           0.0128 |
| Poisson-count |      2 |   0.0194 |    0.9628 |           0.0011 |
| Poisson-count |      3 |   0.4022 |    0.8227 |           0.1492 |
| Poisson-count |      4 |   0.2760 |    0.8442 |           0.0393 |
| NegBin-count  |      1 |   0.1311 |    0.8651 |           0.0128 |
| NegBin-count  |      2 |   0.0117 |    0.9430 |           0.0011 |
| NegBin-count  |      3 |   0.5400 |    0.8583 |           0.1492 |
| NegBin-count  |      4 |   0.2493 |    0.8512 |           0.0393 |

## 9. Calibration (Brier score, test)

| model        |   Platt |   isotonic |   uncalibrated |
|:-------------|--------:|-----------:|---------------:|
| LightGBM     | 0.07592 |    0.07585 |        0.13499 |
| LogReg-L1    | 0.07757 |    0.07649 |        0.15299 |
| LogReg-L2    | 0.07782 |    0.07674 |        0.15438 |
| MLP          | 0.08497 |    0.08413 |        0.10613 |
| RandomForest | 0.08023 |    0.07953 |        0.08934 |
| XGBoost      | 0.07592 |    0.07586 |        0.13619 |

PR-AUC after calibration:

| model        |   Platt |   isotonic |   uncalibrated |
|:-------------|--------:|-----------:|---------------:|
| LightGBM     |  0.3864 |     0.3847 |         0.3823 |
| LogReg-L1    |  0.3775 |     0.3774 |         0.3761 |
| LogReg-L2    |  0.3715 |     0.3703 |         0.3708 |
| MLP          |  0.2437 |     0.2441 |         0.1855 |
| RandomForest |  0.3425 |     0.3435 |         0.3340 |
| XGBoost      |  0.3876 |     0.3872 |         0.3809 |

## 10. Interpretability

LogReg-L1 non-zero coefficients: 300 of 545

### Top 20 features per model

|    | LogReg-L1   | LogReg-L2   | Bayesian-LR (horseshoe)   | RandomForest   | XGBoost    | LightGBM   |
|---:|:------------|:------------|:--------------------------|:---------------|:-----------|:-----------|
|  1 | aux_19      | summer      | house                     | flu            | flu        | aux_19     |
|  2 | summer      | swine       | family                    | sick           | jab        | flu        |
|  3 | swine       | aux_19      | tested                    | aux_19         | vai        | swine      |
|  4 | tested      | stomach     | strep                     | aux_17         | aku        | stomach    |
|  5 | jab         | jab         | aux_19                    | aux_18         | lagi       | summer     |
|  6 | stomach     | allergies   | season                    | aux_15         | condom     | bird       |
|  7 | allergies   | tested      | test                      | aux_14         | summer     | aux_02     |
|  8 | flu         | flu         | flu                       | house          | banget     | house      |
|  9 | aux_02      | family      | aux_18                    | aux_12         | slime      | aux_16     |
| 10 | 2013        | bird        | aux_07                    | aux_13         | strep      | around     |
| 11 | family      | house       | around                    | aux_16         | gini       | cold       |
| 12 | bird        | aux_18      | bronchitis                | around         | ini        | family     |
| 13 | house       | 2013        | dad                       | aux_10         | 12s        | aux_17     |
| 14 | snow        | snow        | aux_17                    | swine          | doctor     | sick       |
| 15 | spring      | spring      | feeling                   | aux_07         | sick       | sucks      |
| 16 | around      | around      | 2013                      | aux_08         | work       | symptoms   |
| 17 | pra         | thera       | aux_16                    | aux_11         | aux_19     | allergies  |
| 18 | tea         | aux_17      | aux_08                    | aux_06         | pra        | aux_00     |
| 19 | thera       | tea         | stay                      | home           | bgt        | aux_01     |
| 20 | swag        | holidays    | doctor                    | sucks          | bronchitis | year       |

### LogReg-L2 largest positive coefficients

|          |   coef |
|:---------|-------:|
| aux_19   | 2.1190 |
| tested   | 1.6601 |
| flu      | 1.5662 |
| family   | 1.5107 |
| house    | 1.3733 |
| aux_18   | 1.3637 |
| 2013     | 1.3391 |
| snow     | 1.3320 |
| around   | 1.2766 |
| aux_17   | 1.2363 |
| holidays | 1.1333 |
| aux_16   | 1.0665 |
| brother  | 1.0056 |
| meds     | 0.9883 |
| strep    | 0.9868 |

### LogReg-L2 largest negative coefficients

|           |    coef |
|:----------|--------:|
| summer    | -2.5738 |
| swine     | -2.3071 |
| stomach   | -1.8086 |
| jab       | -1.7903 |
| allergies | -1.6605 |
| bird      | -1.4266 |
| spring    | -1.3130 |
| thera     | -1.2681 |
| tea       | -1.2100 |
| swag      | -1.1266 |
| aux_02    | -1.0984 |
| pra       | -1.0498 |
| fly       | -1.0344 |
| jordan    | -1.0130 |
| symptoms  | -0.9945 |

### Top-20 overlap (Jaccard)

|                         |   LogReg-L1 |   LogReg-L2 |   Bayesian-LR (horseshoe) |   RandomForest |   XGBoost |   LightGBM |
|:------------------------|------------:|------------:|--------------------------:|---------------:|----------:|-----------:|
| LogReg-L1               |       1.000 |       0.739 |                     0.212 |          0.143 |     0.143 |      0.379 |
| LogReg-L2               |       0.739 |       1.000 |                     0.290 |          0.212 |     0.111 |      0.379 |
| Bayesian-LR (horseshoe) |       0.212 |       0.290 |                     1.000 |          0.290 |     0.143 |      0.212 |
| RandomForest            |       0.143 |       0.212 |                     0.290 |          1.000 |     0.081 |      0.290 |
| XGBoost                 |       0.143 |       0.111 |                     0.143 |          0.081 |     1.000 |      0.111 |
| LightGBM                |       0.379 |       0.379 |                     0.212 |          0.290 |     0.111 |      1.000 |

### Spearman correlation of |importance| (all features)

|                         |   LogReg-L1 |   LogReg-L2 |   Bayesian-LR (horseshoe) |   RandomForest |   XGBoost |   LightGBM |
|:------------------------|------------:|------------:|--------------------------:|---------------:|----------:|-----------:|
| LogReg-L1               |       1.000 |       0.856 |                     0.195 |          0.298 |     0.533 |      0.727 |
| LogReg-L2               |       0.856 |       1.000 |                     0.220 |          0.158 |     0.499 |      0.718 |
| Bayesian-LR (horseshoe) |       0.195 |       0.220 |                     1.000 |          0.462 |     0.266 |      0.372 |
| RandomForest            |       0.298 |       0.158 |                     0.462 |          1.000 |     0.311 |      0.543 |
| XGBoost                 |       0.533 |       0.499 |                     0.266 |          0.311 |     1.000 |      0.576 |
| LightGBM                |       0.727 |       0.718 |                     0.372 |          0.543 |     0.576 |      1.000 |

### Consensus top 20 (mean rank across models)

|            |   mean_rank |
|:-----------|------------:|
| flu        |        4.67 |
| aux_19     |        5.00 |
| house      |       13.50 |
| family     |       16.33 |
| around     |       16.83 |
| strep      |       23.17 |
| sick       |       23.17 |
| tested     |       28.17 |
| doctor     |       31.67 |
| stay       |       36.00 |
| care       |       46.17 |
| aux_08     |       47.00 |
| season     |       49.67 |
| 2013       |       51.83 |
| aux_16     |       52.00 |
| sucks      |       54.50 |
| year       |       57.17 |
| summer     |       59.33 |
| swine      |       59.83 |
| bronchitis |       60.83 |

## 11. Compute time

|                         |   tuning_s |   fit_s |   predict_test_s |   predict_per_1k_ms |
|:------------------------|-----------:|--------:|-----------------:|--------------------:|
| LightGBM                |     56.470 |   0.778 |            0.034 |               1.467 |
| XGBoost                 |     34.968 |   0.714 |            0.035 |               1.492 |
| LogReg-L1               |     17.736 |   3.977 |            0.016 |               0.706 |
| LogReg-L2               |      1.383 |   0.277 |            0.011 |               0.473 |
| RandomForest            |    153.075 |  10.362 |            0.103 |               4.413 |
| NegBin-count            |      0.000 |   2.392 |            0.009 |               0.380 |
| Bayesian-LR (horseshoe) |      0.000 |  91.572 |            0.210 |               9.014 |
| Poisson-count           |      0.000 |   1.287 |            0.009 |               0.390 |
| MLP                     |     59.282 |  46.476 |            0.050 |               2.162 |

Environment: {"python": "3.13.5", "sklearn": "1.9.1", "lightgbm": "4.7.0", "xgboost": "3.4.1", "shap": "0.54.1", "cpu_cores": 8, "platform": "Linux-6.12.113+-x86_64-with-glibc2.41", "pymc": "6.4.0"}

## 12. Figures

| Figure   | file                                                   | title                                                                                                         |
|:---------|:-------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|
| 4.1      | figures/fig4_01_sparsity_histograms.png                | Distribution of feature-level and observation-level sparsity (training set)                                   |
| 4.2      | figures/fig4_02_top_keywords.png                       | Top 20 Twitter keywords by total count (training set)                                                         |
| 4.3      | figures/fig4_03_sparsity_heatmap.png                   | Sparsity heatmap: non-zero cells (black) in a random sample of observations                                   |
| 4.4      | figures/fig4_04_prevalence_by_state.png                | Outbreak prevalence by state, train vs. test split                                                            |
| 4.5      | figures/fig4_05_prevalence_over_time.png               | Share of states labelled as outbreak at each time step (seasonality)                                          |
| 4.6      | figures/fig4_06_model_comparison_auc.png               | Test-set PR-AUC and ROC-AUC by model (blue = statistical, red = ML)                                           |
| 4.7      | figures/fig4_07_model_comparison_threshold_metrics.png | Threshold-dependent test metrics (threshold tuned on training OOF predictions)                                |
| 4.8      | figures/fig4_08_pr_curves.png                          | Precision-recall curves on the test split                                                                     |
| 4.9      | figures/fig4_09_per_state_pr_auc.png                   | Per-state test PR-AUC: best statistical vs. best ML model                                                     |
| 4.10     | figures/fig4_10_dr_imbalance.png                       | Effect of dimensionality reduction and imbalance-handling strategy on test PR-AUC                             |
| 4.11     | figures/fig4_11_sparsity_experiments.png               | Model performance vs. feature sparsity (feature counts annotated in left panel)                               |
| 4.12     | figures/fig4_12_cv_vs_temporal_vs_test.png             | PR-AUC under shuffled CV, temporal CV and the held-out test split                                             |
| 4.13     | figures/fig4_13_calibration_curves.png                 | Reliability diagrams on the test split (uncalibrated)                                                         |
| 4.14     | figures/fig4_14_calibration_posthoc.png                | Effect of post-hoc Platt and isotonic calibration on reliability (test split)                                 |
| 4.15     | figures/fig4_15_logistic_coefficients.png              | Keyword effects in the statistical models                                                                     |
| 4.16     | figures/fig4_16_shap_summary.png                       | SHAP summary for LightGBM (3,000 random test rows, top 20 features)                                           |
| 4.17     | figures/fig4_17_ml_feature_importance.png              | Top 20 features by importance in the tree-based ML models                                                     |
| 4.18     | figures/fig4_18_runtime.png                            | Training time per model (8 CPU cores; excludes tuning)                                                        |
| 4.19     | figures/fig4_19_temporal_features_validation.png       | Lagged/rolling temporal features: validation vs. test PR-AUC, and ensemble weight chosen on validation        |
| 4.20     | figures/fig4_20_reliability_validation_calibrated.png  | Reliability diagrams on the test split after calibration fitted on the validation block (10 quantile bins)    |
| 4.21     | figures/fig4_21_operating_points.png                   | Operating points chosen on validation (best F1, best MCC, early warning) and their test performance           |
| 4.22     | figures/fig4_22_bootstrap_ci_forest.png                | Test metrics with 95% circular block-bootstrap CIs (block = 28 steps, B = 2000, all states resampled jointly) |
| 4.23     | figures/fig4_23_paired_differences.png                 | Paired model comparisons: block-bootstrap CIs of the difference, bootstrap and DeLong p-values (unadjusted)   |
| 4.24     | figures/fig4_24_improved_model_features.png            | Top 25 features of the two members of the improved Twitter-only ensemble                                      |

---

## 13. Notes, caveats and deviations from the proposal (written after reading the outputs above)

**Data structure**
* The X matrices have 545 columns, but `flu_keywords` lists 525. Columns 20–544 line up with the keywords in order (column 20 = "flu" has the largest total).
  Columns 0–19 are undocumented and non-decreasing within every row (aux_monotone_frac = 1.0). They were kept as `aux_00`–`aux_19`.
  They carry a lot of signal: dropping them lowers test PR-AUC from 0.3708 to 0.3393 (LogReg-L2) and from 0.3823 to 0.3396 (LightGBM) (§7.1), and `aux_19` ranks near the top in most importance lists.
  Because their meaning is unknown, this is a limitation for interpretation.
* Each state has 1,095 training rows and 485 test rows (48 × 1,580 = 75,840 against 75,839 on UCI). Labels are piecewise constant, and 78.8% of positive runs are multiples of 7 rows.
  This fits weekly CDC labels on rows that look like daily-indexed sliding windows. UCI calls each row a state-week, with the label = outbreak in the following week. The notebook uses the neutral term "time step".
* The proposal planned an 80/20 stratified split. The **provided temporal split** was used instead (train = first 1,095 steps, test = last 485), as instructed. Prevalence differs: 5.53% in train and 9.80% in test.

**Evaluation**
* Thresholds for F1, precision, recall, MCC and balanced accuracy were tuned on training OOF predictions (max F1), never on test data.
* Shuffled stratified CV on autocorrelated, overlapping time steps is optimistic. Forward-chaining temporal CV gave much lower PR-AUC for every model (for example LightGBM 0.1628 against 0.3843 OOF) (§8).
  Part of this gap comes from very low validation prevalence in temporal folds 1–2 (1.28% and 0.11%), so the fold values should be read with care.
* Nested CV (proposal 3.5) was **not** run because of compute time. Single-level 5-fold CV tuning plus the held-out test split was used.
* The differences between the top four models on test PR-AUC are small (0.3708–0.3823). Section 14 adds block-bootstrap CIs and paired tests: the LightGBM vs. LogReg-L1 baseline difference is not significant, so in sections 4–11 "best" means best point estimate on this split.

**Models (deviations)**
* **Poisson / NB**: implemented as generative count classifiers on total keyword volume with state fixed effects (see notebook §5.2). The Poisson model's posteriors are extremely
  over-confident: its tuned threshold is 1.0000 because overdispersion is ignored. NB (α = 0.6168) is better behaved. In temporal CV the count models had the highest ROC-AUC (NB 0.8794).
* **Bayesian LR**: full-data NUTS over 545 features was not feasible (a 50-feature NUTS test did not finish in about 11 minutes). Instead the model used a horseshoe prior on the top-50 χ² features with
  **mean-field ADVI** (PyMC 6.4.0), which tends to underestimate posterior uncertainty. Its threshold was tuned on in-sample training predictions, not OOF.
* **PCA** was replaced by **TruncatedSVD** (sparse input). 300 components (the cap) did not reach 95% explained variance, so the SVD rows use 300 components.
* **MLP**: scikit-learn MLP (128, 64), with an L2 penalty instead of dropout, early stopping, and random oversampling for imbalance. It performed poorly (test ROC-AUC 0.5368), so the result reflects this specific set-up and is not a general verdict on neural networks.
  The LSTM in the proposal was optional and was not run.
* **RF** tuning grid was reduced (max_features fixed to "sqrt") to save compute time.
* **XGBoost** importance includes several rare non-English tokens (for example "vai", "aku", "lagi", "banget") among its top 20 by mean |SHAP|. This suggests some splits on rare tokens and is worth discussing as possible spurious signal.

**Calibration**
* Class-weighted models over-predict risk before calibration (Brier score 0.13–0.15). Platt and isotonic calibration roughly halve the Brier score (for example LightGBM 0.1350 → 0.0759 with Platt).
  After calibration, the reliability curves *under*-predict on test, which fits the higher test prevalence (9.80% against 5.53%).

**Live X dashboard** (prototype only): an illustration, with no labels and no evaluation. None of its numbers belong in the results chapter.


## 14. Improved models and statistical validation (strictly temporal protocol)

*Added after the first submission draft. Every choice in this section (feature set, LightGBM/LogReg-L1 settings, calibrator, ensemble weight, thresholds) was made on a validation block carved from the end of the training period. The test split was scored once at the end.*

### 14.1 Protocol

|                                     | value                                                                                        |
|:------------------------------------|:---------------------------------------------------------------------------------------------|
| val_steps                           | 657-1094                                                                                     |
| n_val                               | 21024                                                                                        |
| val_positives                       | 1981                                                                                         |
| val_prevalence                      | 0.09422564687975647                                                                          |
| origin1_train_steps                 | 0-656                                                                                        |
| origin2_train_steps                 | 0-875                                                                                        |
| validation_origins                  | train on steps before the block, predict the block (two rolling origins, pooled)             |
| temporal_feature_columns            | 781                                                                                          |
| label_history_columns               | y_lag14, y_lag21, y_lag14_mean28                                                             |
| label_history_reporting_delay_steps | 14                                                                                           |
| ensemble_weight_on_lightgbm         | 0.45                                                                                         |
| recommended_twitter_only_model      | Ensemble (calibrated LightGBM + LogReg-L1)                                                   |
| bootstrap                           | circular block bootstrap, L = 28 steps, B = 2000, seed = 42, all 48 states resampled jointly |

Boundary check (train and test are one contiguous series per state):

|                             |    value |
|:----------------------------|---------:|
| cos_last_two_train_steps    | 0.725547 |
| cos_last_train_first_test   | 0.714928 |
| cos_random_train_test_pair  | 0.504351 |
| label_agreement_at_boundary | 1.000000 |

### 14.2 Validation grid (best setting per model and feature set)

|                                                  | settings                                                          |   n_features |   val_pr_auc |   val_roc_auc |
|:-------------------------------------------------|:------------------------------------------------------------------|-------------:|-------------:|--------------:|
| ('LightGBM', 'base (545)')                       | {"num_leaves": 7, "min_child_samples": 200, "n_estimators": 200}  |          545 |     0.285991 |      0.733206 |
| ('LightGBM', 'base + temporal')                  | {"num_leaves": 31, "min_child_samples": 200, "n_estimators": 200} |         1326 |     0.336014 |      0.730160 |
| ('LightGBM', 'base + temporal + label history')  | {"num_leaves": 31, "min_child_samples": 200, "n_estimators": 100} |         1329 |     0.562286 |      0.834124 |
| ('LogReg-L1', 'base (545)')                      | {"C": 0.03}                                                       |          545 |     0.399023 |      0.813650 |
| ('LogReg-L1', 'base + temporal')                 | {"C": 0.005}                                                      |         1326 |     0.441696 |      0.851925 |
| ('LogReg-L1', 'base + temporal + label history') | {"C": 0.01}                                                       |         1329 |     0.568808 |      0.892365 |

Reference points on the same validation rows:

| model                                | feature_set        | settings   |   n_features |   val_pr_auc |   val_roc_auc |
|:-------------------------------------|:-------------------|:-----------|-------------:|-------------:|--------------:|
| Persistence (label 14 steps earlier) | label history      | none       |            1 |     0.399928 |      0.763551 |
| LogReg-L1                            | label history only | {"C": 1.0} |            3 |     0.454460 |      0.839516 |

Full grid: `results/improve_validation_grid.csv`.


### 14.3 Validation and test results (calibrated; thresholds = best validation F1)

| model                                       | feature_set                     | uses_label_history   |   val_pr_auc_raw |   val_pr_auc_calibrated |   val_roc_auc_calibrated |   test_pr_auc_raw |   test_roc_auc_raw | calibration   |   test_pr_auc_calibrated |   test_roc_auc_calibrated |   test_brier_uncalibrated |   test_brier_calibrated |   threshold_best_f1 |   test_f1 |   test_mcc |   test_precision |   test_recall |
|:--------------------------------------------|:--------------------------------|:---------------------|-----------------:|------------------------:|-------------------------:|------------------:|-------------------:|:--------------|-------------------------:|--------------------------:|--------------------------:|------------------------:|--------------------:|----------:|-----------:|-----------------:|--------------:|
| LightGBM \| base (545)                       | base (545)                      | False                |         0.285991 |                0.285991 |                 0.733206 |          0.361561 |           0.788283 | Platt         |                 0.361561 |                  0.788283 |                  0.149143 |                0.076045 |            0.152951 |  0.396403 |   0.324449 |         0.346204 |      0.463628 |
| LightGBM \| base + temporal                  | base + temporal                 | False                |         0.336014 |                0.336014 |                 0.730160 |          0.514190 |           0.855286 | Platt         |                 0.514190 |                  0.855286 |                  0.067709 |                0.070507 |            0.172238 |  0.382187 |   0.349621 |         0.249698 |      0.814198 |
| LightGBM \| base + temporal + label history  | base + temporal + label history | True                 |         0.562286 |                0.562286 |                 0.834124 |          0.628836 |           0.917617 | Platt         |                 0.628836 |                  0.917617 |                  0.062935 |                0.055763 |            0.327063 |  0.650436 |   0.616703 |         0.555556 |      0.784400 |
| LogReg-L1 \| base (545)                      | base (545)                      | False                |         0.399023 |                0.399023 |                 0.813650 |          0.370651 |           0.788213 | Platt         |                 0.370651 |                  0.788213 |                  0.153918 |                0.076477 |            0.166864 |  0.376784 |   0.318827 |         0.420399 |      0.341367 |
| LogReg-L1 \| base + temporal                 | base + temporal                 | False                |         0.441696 |                0.441696 |                 0.851925 |          0.429097 |           0.853307 | Platt         |                 0.429097 |                  0.853307 |                  0.155351 |                0.070287 |            0.261313 |  0.439139 |   0.383858 |         0.471357 |      0.411043 |
| LogReg-L1 \| base + temporal + label history | base + temporal + label history | True                 |         0.568808 |                0.568808 |                 0.892365 |          0.660423 |           0.924193 | Platt         |                 0.660423 |                  0.924193 |                  0.106971 |                0.051070 |            0.167187 |  0.654891 |   0.618748 |         0.577942 |      0.755478 |
| LightGBM (baseline)                         | base (545)                      | False                |         0.210344 |                0.200117 |                 0.642244 |          0.382267 |           0.788750 | isotonic      |                 0.352840 |                  0.769785 |                  0.134990 |                0.075391 |            0.148867 |  0.394981 |   0.326074 |         0.305462 |      0.558720 |
| LogReg-L1 (baseline)                        | base (545)                      | False                |         0.370993 |                0.360332 |                 0.785760 |          0.376068 |           0.794664 | isotonic      |                 0.357812 |                  0.792435 |                  0.152987 |                0.075374 |            0.203863 |  0.395772 |   0.332157 |         0.406467 |      0.385627 |
| LogReg-L1 \| label history only              | label history only              | True                 |         0.454460 |                0.454460 |                 0.839516 |          0.463752 |           0.823061 | Platt         |                 0.463752 |                  0.823061 |                  0.130957 |                0.058355 |            0.107095 |  0.631897 |   0.590697 |         0.584575 |      0.687555 |
| Ensemble (calibrated LightGBM + LogReg-L1)  | Twitter-only                    | False                |       nan        |                0.469692 |                 0.836241 |        nan        |         nan        | ensemble      |                 0.494325 |                  0.866587 |                nan        |                0.066601 |            0.219549 |  0.495499 |   0.437573 |         0.433115 |      0.578878 |
| Persistence (label 14 steps earlier)        | label history                   | True                 |         0.399928 |              nan        |                 0.763551 |          0.443468 |           0.814312 | none          |               nan        |                nan        |                  0.074270 |              nan        |            0.500000 |  0.640765 |   0.600472 |         0.609245 |      0.675723 |

Settings:

| model                                       | settings                                                                           |
|:--------------------------------------------|:-----------------------------------------------------------------------------------|
| LightGBM \| base (545)                       | {"num_leaves": 7, "min_child_samples": 200, "n_estimators": 200}                   |
| LightGBM \| base + temporal                  | {"num_leaves": 31, "min_child_samples": 200, "n_estimators": 200}                  |
| LightGBM \| base + temporal + label history  | {"num_leaves": 31, "min_child_samples": 200, "n_estimators": 100}                  |
| LogReg-L1 \| base (545)                      | {"C": 0.03}                                                                        |
| LogReg-L1 \| base + temporal                 | {"C": 0.005}                                                                       |
| LogReg-L1 \| base + temporal + label history | {"C": 0.01}                                                                        |
| LightGBM (baseline)                         | {"num_leaves": 15, "min_child_samples": 20, "n_estimators": 400} (sections 5-7)    |
| LogReg-L1 (baseline)                        | {"C": 0.1} (sections 5-7)                                                          |
| LogReg-L1 \| label history only              | {"C": 1.0}                                                                         |
| Ensemble (calibrated LightGBM + LogReg-L1)  | w_LightGBM=0.45; members: LightGBM \| base + temporal + LogReg-L1 \| base + temporal |
| Persistence (label 14 steps earlier)        | none                                                                               |

### 14.4 Calibration (fitted on validation; method chosen by cross-fitted validation Brier)

| model                                       |   val_brier_uncalibrated |   test_brier_uncalibrated |   val_brier_Platt_crossfit |   test_brier_Platt |   test_pr_auc_Platt |   val_brier_isotonic_crossfit |   test_brier_isotonic |   test_pr_auc_isotonic | chosen_on_validation   |
|:--------------------------------------------|-------------------------:|--------------------------:|---------------------------:|-------------------:|--------------------:|------------------------------:|----------------------:|-----------------------:|:-----------------------|
| LightGBM \| base (545)                       |                 0.172094 |                  0.149143 |                   0.081662 |           0.076045 |            0.361561 |                      0.082064 |              0.075994 |               0.346302 | Platt                  |
| LightGBM \| base + temporal                  |                 0.079486 |                  0.067709 |                   0.096190 |           0.070507 |            0.514190 |                      0.097899 |              0.070442 |               0.484655 | Platt                  |
| LightGBM \| base + temporal + label history  |                 0.058679 |                  0.062935 |                   0.062356 |           0.055763 |            0.628836 |                      0.064492 |              0.056673 |               0.605814 | Platt                  |
| LogReg-L1 \| base (545)                      |                 0.191274 |                  0.153918 |                   0.071871 |           0.076477 |            0.370651 |                      0.072058 |              0.076129 |               0.354346 | Platt                  |
| LogReg-L1 \| base + temporal                 |                 0.181593 |                  0.155351 |                   0.066545 |           0.070287 |            0.429097 |                      0.068596 |              0.070715 |               0.413138 | Platt                  |
| LogReg-L1 \| base + temporal + label history |                 0.102356 |                  0.106971 |                   0.065500 |           0.051070 |            0.660423 |                      0.066122 |              0.051883 |               0.604962 | Platt                  |
| LightGBM (baseline)                         |                 0.136409 |                  0.134990 |                   0.091647 |           0.081625 |            0.382267 |                      0.089443 |              0.075391 |               0.352840 | isotonic               |
| LogReg-L1 (baseline)                        |                 0.179029 |                  0.152987 |                   0.075837 |           0.075969 |            0.376068 |                      0.074821 |              0.075374 |               0.357812 | isotonic               |
| LogReg-L1 \| label history only              |                 0.122958 |                  0.130957 |                   0.070925 |           0.058355 |            0.463752 |                      0.080349 |              0.060648 |               0.445051 | Platt                  |

### 14.5 Operating points (chosen on validation, applied unchanged to test)

| model                                       | operating_point                    |   threshold |   val_f1 |   val_mcc |   val_precision |   val_recall |   test_f1 |   test_mcc |   test_precision |   test_recall |   test_balanced_acc |   test_alerts_per_1000 |
|:--------------------------------------------|:-----------------------------------|------------:|---------:|----------:|----------------:|-------------:|----------:|-----------:|-----------------:|--------------:|--------------------:|-----------------------:|
| LightGBM \| base (545)                       | best F1                            |    0.152951 | 0.326515 |  0.246745 |        0.259857 |     0.439172 |  0.396403 |   0.324449 |         0.346204 |      0.463628 |            0.684238 |             131.271478 |
| LightGBM \| base (545)                       | best MCC                           |    0.224130 | 0.310497 |  0.247502 |        0.342892 |     0.283695 |  0.372386 |   0.319637 |         0.438056 |      0.323839 |            0.639346 |              72.465636 |
| LightGBM \| base (545)                       | early warning (val recall >= 0.80) |    0.061384 | 0.246885 |  0.183038 |        0.145962 |     0.800101 |  0.294923 |   0.243957 |         0.180687 |      0.801928 |            0.703374 |             435.051546 |
| LightGBM \| base + temporal                  | best F1                            |    0.172238 | 0.363200 |  0.290246 |        0.319647 |     0.420495 |  0.382187 |   0.349621 |         0.249698 |      0.814198 |            0.774158 |             319.630584 |
| LightGBM \| base + temporal                  | best MCC                           |    0.172238 | 0.363200 |  0.290246 |        0.319647 |     0.420495 |  0.382187 |   0.349621 |         0.249698 |      0.814198 |            0.774158 |             319.630584 |
| LightGBM \| base + temporal                  | early warning (val recall >= 0.80) |    0.059996 | 0.232712 |  0.159869 |        0.136157 |     0.800101 |  0.204845 |   0.130709 |         0.114202 |      0.992989 |            0.577978 |             852.319588 |
| LightGBM \| base + temporal + label history  | best F1                            |    0.327063 | 0.574468 |  0.536213 |        0.624926 |     0.531550 |  0.650436 |   0.616703 |         0.555556 |      0.784400 |            0.858101 |             138.402062 |
| LightGBM \| base + temporal + label history  | best MCC                           |    0.379052 | 0.571757 |  0.540231 |        0.664439 |     0.501767 |  0.660121 |   0.625048 |         0.579960 |      0.765995 |            0.852852 |             129.467354 |
| LightGBM \| base + temporal + label history  | early warning (val recall >= 0.80) |    0.050644 | 0.325328 |  0.287952 |        0.204174 |     0.800101 |  0.268041 |   0.243610 |         0.155400 |      0.974145 |            0.699379 |             614.475945 |
| LogReg-L1 \| base (545)                      | best F1                            |    0.166864 | 0.429072 |  0.364906 |        0.378817 |     0.494700 |  0.376784 |   0.318827 |         0.420399 |      0.341367 |            0.645110 |              79.596220 |
| LogReg-L1 \| base (545)                      | best MCC                           |    0.185425 | 0.428137 |  0.364986 |        0.398607 |     0.462393 |  0.364664 |   0.314103 |         0.440447 |      0.311131 |            0.634087 |              69.243986 |
| LogReg-L1 \| base (545)                      | early warning (val recall >= 0.80) |    0.064719 | 0.309752 |  0.269186 |        0.192051 |     0.800101 |  0.353659 |   0.293869 |         0.239782 |      0.673532 |            0.720731 |             275.343643 |
| LogReg-L1 \| base + temporal                 | best F1                            |    0.261313 | 0.483675 |  0.426950 |        0.449502 |     0.523473 |  0.439139 |   0.383858 |         0.471357 |      0.411043 |            0.680471 |              85.481100 |
| LogReg-L1 \| base + temporal                 | best MCC                           |    0.261313 | 0.483675 |  0.426950 |        0.449502 |     0.523473 |  0.439139 |   0.383858 |         0.471357 |      0.411043 |            0.680471 |              85.481100 |
| LogReg-L1 \| base + temporal                 | early warning (val recall >= 0.80) |    0.070632 | 0.356300 |  0.323432 |        0.229179 |     0.800101 |  0.399491 |   0.357575 |         0.271370 |      0.756792 |            0.767981 |             273.367698 |
| LogReg-L1 \| base + temporal + label history | best F1                            |    0.167187 | 0.624217 |  0.584849 |        0.620020 |     0.628470 |  0.654891 |   0.618748 |         0.577942 |      0.755478 |            0.847760 |             128.135739 |
| LogReg-L1 \| base + temporal + label history | best MCC                           |    0.167187 | 0.624217 |  0.584849 |        0.620020 |     0.628470 |  0.654891 |   0.618748 |         0.577942 |      0.755478 |            0.847760 |             128.135739 |
| LogReg-L1 \| base + temporal + label history | early warning (val recall >= 0.80) |    0.068084 | 0.507444 |  0.478940 |        0.371542 |     0.800101 |  0.513761 |   0.498014 |         0.362199 |      0.883436 |            0.857186 |             239.089347 |
| LightGBM (baseline)                         | best F1                            |    0.148867 | 0.272746 |  0.184627 |        0.226484 |     0.342756 |  0.394981 |   0.326074 |         0.305462 |      0.558720 |            0.710330 |             179.295533 |
| LightGBM (baseline)                         | best MCC                           |    0.170732 | 0.265252 |  0.185263 |        0.253924 |     0.277638 |  0.405638 |   0.334874 |         0.348318 |      0.485539 |            0.693408 |             136.640893 |
| LightGBM (baseline)                         | early warning (val recall >= 0.80) |    0.065262 | 0.172276 |  0.005886 |        0.094257 |     1.000000 |  0.178546 |   0.000000 |         0.098024 |      1.000000 |            0.500000 |            1000.000000 |
| LogReg-L1 (baseline)                        | best F1                            |    0.203863 | 0.401639 |  0.333710 |        0.350659 |     0.469965 |  0.395772 |   0.332157 |         0.406467 |      0.385627 |            0.662215 |              92.998282 |
| LogReg-L1 (baseline)                        | best MCC                           |    0.289474 | 0.390863 |  0.338386 |        0.442812 |     0.349823 |  0.339229 |   0.311555 |         0.501285 |      0.256354 |            0.614319 |              50.128866 |
| LogReg-L1 (baseline)                        | early warning (val recall >= 0.80) |    0.048969 | 0.274010 |  0.226138 |        0.164536 |     0.818778 |  0.311258 |   0.262013 |         0.194069 |      0.785714 |            0.715555 |             396.864261 |
| LogReg-L1 \| label history only              | best F1                            |    0.107095 | 0.606782 |  0.567257 |        0.622742 |     0.591620 |  0.631897 |   0.590697 |         0.584575 |      0.687555 |            0.817227 |             115.292096 |
| LogReg-L1 \| label history only              | best MCC                           |    0.107095 | 0.606782 |  0.567257 |        0.622742 |     0.591620 |  0.631897 |   0.590697 |         0.584575 |      0.687555 |            0.817227 |             115.292096 |
| LogReg-L1 \| label history only              | early warning (val recall >= 0.80) |    0.045550 | 0.296834 |  0.268273 |        0.178615 |     0.877839 |  0.186050 |   0.059477 |         0.102812 |      0.977213 |            0.525229 |             931.701031 |
| Ensemble (calibrated LightGBM + LogReg-L1)  | best F1                            |    0.219549 | 0.495923 |  0.441259 |        0.472362 |     0.521959 |  0.495499 |   0.437573 |         0.433115 |      0.578878 |            0.748269 |             131.013746 |
| Ensemble (calibrated LightGBM + LogReg-L1)  | best MCC                           |    0.219549 | 0.495923 |  0.441259 |        0.472362 |     0.521959 |  0.495499 |   0.437573 |         0.433115 |      0.578878 |            0.748269 |             131.013746 |
| Ensemble (calibrated LightGBM + LogReg-L1)  | early warning (val recall >= 0.80) |    0.086253 | 0.360145 |  0.327699 |        0.232371 |     0.800101 |  0.334606 |   0.309860 |         0.206388 |      0.883436 |            0.757129 |             419.587629 |

### 14.6 95% block-bootstrap confidence intervals (test)

F1 and MCC use each model's best-F1 threshold (baselines: the training-OOF threshold from section 4). Median positive run length in test: 21.0 steps; autocorrelation of the cross-state outbreak share at lags 1/7/14/28/56: 0.989770, 0.929140, 0.813279, 0.607674, 0.039671.

|                                                          | PR-AUC                  | ROC-AUC                 | F1                      | MCC                     |
|:---------------------------------------------------------|:------------------------|:------------------------|:------------------------|:------------------------|
| LightGBM (baseline)                                      | 0.3823 [0.2003, 0.5016] | 0.7887 [0.7283, 0.8480] | 0.3956 [0.2579, 0.4764] | 0.3386 [0.2221, 0.4197] |
| LogReg-L1 (baseline)                                     | 0.3761 [0.2016, 0.4936] | 0.7947 [0.7332, 0.8538] | 0.3639 [0.2385, 0.4370] | 0.3203 [0.2113, 0.3928] |
| LogReg-L1 \| base + temporal [calibrated]                 | 0.4291 [0.2205, 0.5343] | 0.8533 [0.7948, 0.8998] | 0.4391 [0.2728, 0.5207] | 0.3839 [0.2430, 0.4618] |
| LightGBM \| base + temporal [calibrated]                  | 0.5142 [0.3221, 0.6262] | 0.8553 [0.7968, 0.9074] | 0.3822 [0.1884, 0.5098] | 0.3496 [0.2227, 0.4278] |
| Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]  | 0.4943 [0.3060, 0.5935] | 0.8666 [0.8102, 0.9134] | 0.4955 [0.3385, 0.5771] | 0.4376 [0.3132, 0.5162] |
| LogReg-L1 \| base + temporal + label history [calibrated] | 0.6604 [0.5237, 0.7224] | 0.9242 [0.8931, 0.9535] | 0.6549 [0.5600, 0.6959] | 0.6187 [0.5471, 0.6574] |
| LogReg-L1 \| label history only [calibrated]              | 0.4638 [0.3452, 0.5341] | 0.8231 [0.7542, 0.8962] | 0.6319 [0.5324, 0.6748] | 0.5907 [0.5176, 0.6384] |
| Persistence (label 14 steps earlier)                     | 0.4435 [0.3242, 0.5082] | 0.8143 [0.7424, 0.8914] | 0.6408 [0.5422, 0.6814] | 0.6005 [0.5261, 0.6497] |

Raw values: `results/improve_bootstrap_ci.csv`.


### 14.7 Paired significance tests (test split)

p_block_bootstrap = two-sided percentile p-value of the paired block-bootstrap difference; Holm-adjusted within each metric. DeLong assumes independent rows and therefore understates the uncertainty for these autocorrelated data; the block bootstrap is the primary test.

| model_a                                                  | model_b                                     | metric   |   diff_a_minus_b |   boot_ci_low |   boot_ci_high |   p_block_bootstrap |   share_boot_diff_gt0 |   delong_z |    delong_se |       p_delong |   p_block_bootstrap_holm |   p_delong_holm |
|:---------------------------------------------------------|:--------------------------------------------|:---------|-----------------:|--------------:|---------------:|--------------------:|----------------------:|-----------:|-------------:|---------------:|-------------------------:|----------------:|
| LogReg-L1 \| base + temporal [calibrated]                 | LightGBM (baseline)                         | pr_auc   |       0.0468295  |  -0.00881827  |    0.0877782   |           0.085957  |                0.9575 |  nan       | nan          | nan            |                0.171914  |  nan            |
| LogReg-L1 \| base + temporal [calibrated]                 | LightGBM (baseline)                         | roc_auc  |       0.0645573  |   0.0266149   |    0.0982665   |           0.003998  |                0.9985 |   13.2357  |   0.00487753 |   5.46219e-40  |                0.011994  |    2.18488e-39  |
| LogReg-L1 \| base + temporal [calibrated]                 | LightGBM (baseline)                         | f1       |       0.0435553  |  -0.0123633   |    0.0782908   |           0.0949525 |                0.953  |  nan       | nan          | nan            |                0.264868  |  nan            |
| LogReg-L1 \| base + temporal [calibrated]                 | LightGBM (baseline)                         | mcc      |       0.0452095  |  -0.00989056  |    0.077315    |           0.0809595 |                0.96   |  nan       | nan          | nan            |                0.242879  |  nan            |
| LogReg-L1 \| base + temporal [calibrated]                 | LogReg-L1 (baseline)                        | pr_auc   |       0.053029   |  -0.00270549  |    0.0874607   |           0.0549725 |                0.973  |  nan       | nan          | nan            |                0.164918  |  nan            |
| LogReg-L1 \| base + temporal [calibrated]                 | LogReg-L1 (baseline)                        | roc_auc  |       0.0586435  |   0.0236495   |    0.0908027   |           0.0029985 |                0.999  |   13.081   |   0.00448311 |   4.2298e-39   |                0.011994  |    1.26894e-38  |
| LogReg-L1 \| base + temporal [calibrated]                 | LogReg-L1 (baseline)                        | f1       |       0.0752593  |  -0.00126687  |    0.114592    |           0.0529735 |                0.974  |  nan       | nan          | nan            |                0.264868  |  nan            |
| LogReg-L1 \| base + temporal [calibrated]                 | LogReg-L1 (baseline)                        | mcc      |       0.0635237  |  -0.00405374  |    0.0956829   |           0.055972  |                0.9725 |  nan       | nan          | nan            |                0.223888  |  nan            |
| Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]  | LightGBM (baseline)                         | pr_auc   |       0.112057   |   0.0672139   |    0.149958    |           0.0049975 |                0.998  |  nan       | nan          | nan            |                0.0249875 |  nan            |
| Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]  | LightGBM (baseline)                         | roc_auc  |       0.0778375  |   0.0462467   |    0.105119    |           0.001999  |                0.9995 |   16.1083  |   0.00483214 |   2.23153e-58  |                0.011994  |    1.33892e-57  |
| Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]  | LightGBM (baseline)                         | f1       |       0.0999156  |   0.0616392   |    0.125678    |           0.003998  |                0.9985 |  nan       | nan          | nan            |                0.023988  |  nan            |
| Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]  | LightGBM (baseline)                         | mcc      |       0.0989242  |   0.0599309   |    0.133584    |           0.0029985 |                0.999  |  nan       | nan          | nan            |                0.0209895 |  nan            |
| Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]  | LogReg-L1 (baseline)                        | pr_auc   |       0.118257   |   0.0754982   |    0.151769    |           0.005997  |                0.9975 |  nan       | nan          | nan            |                0.0249875 |  nan            |
| Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]  | LogReg-L1 (baseline)                        | roc_auc  |       0.0719236  |   0.0448089   |    0.0969493   |           0.001999  |                0.9995 |   15.9014  |   0.0045231  |   6.19698e-57  |                0.011994  |    3.09849e-56  |
| Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]  | LogReg-L1 (baseline)                        | f1       |       0.13162    |   0.0782434   |    0.161611    |           0.0029985 |                0.999  |  nan       | nan          | nan            |                0.023988  |  nan            |
| Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]  | LogReg-L1 (baseline)                        | mcc      |       0.117238   |   0.0780822   |    0.146163    |           0.001999  |                0.9995 |  nan       | nan          | nan            |                0.015992  |  nan            |
| Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]  | LogReg-L1 \| base + temporal [calibrated]    | pr_auc   |       0.0652276  |   0.0403729   |    0.0964929   |           0.001999  |                0.9995 |  nan       | nan          | nan            |                0.015992  |  nan            |
| Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]  | LogReg-L1 \| base + temporal [calibrated]    | roc_auc  |       0.0132801  |  -0.000102991 |    0.0305014   |           0.0529735 |                0.974  |    6.96447 |   0.00190684 |   3.29643e-12  |                0.105947  |    6.59286e-12  |
| Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]  | LogReg-L1 \| base + temporal [calibrated]    | f1       |       0.0563603  |   0.0308287   |    0.0887603   |           0.0029985 |                0.999  |  nan       | nan          | nan            |                0.023988  |  nan            |
| Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]  | LogReg-L1 \| base + temporal [calibrated]    | mcc      |       0.0537147  |   0.0282052   |    0.0985563   |           0.0029985 |                0.999  |  nan       | nan          | nan            |                0.0209895 |  nan            |
| LightGBM (baseline)                                      | LogReg-L1 (baseline)                        | pr_auc   |       0.00619943 |  -0.00626208  |    0.0157264   |           0.351824  |                0.8245 |  nan       | nan          | nan            |                0.351824  |  nan            |
| LightGBM (baseline)                                      | LogReg-L1 (baseline)                        | roc_auc  |      -0.00591382 |  -0.0129418   |    0.000599255 |           0.0669665 |                0.033  |   -2.24933 |   0.00262915 |   0.0244915    |                0.105947  |    0.0244915    |
| LightGBM (baseline)                                      | LogReg-L1 (baseline)                        | f1       |       0.0317041  |  -0.000704614 |    0.0525732   |           0.057971  |                0.9715 |  nan       | nan          | nan            |                0.264868  |  nan            |
| LightGBM (baseline)                                      | LogReg-L1 (baseline)                        | mcc      |       0.0183142  |  -0.00558637  |    0.038142    |           0.123938  |                0.9385 |  nan       | nan          | nan            |                0.247876  |  nan            |
| LogReg-L1 \| base + temporal + label history [calibrated] | LogReg-L1 \| base + temporal [calibrated]    | pr_auc   |       0.231326   |   0.183682    |    0.310712    |           0.0009995 |                1      |  nan       | nan          | nan            |                0.0089955 |  nan            |
| LogReg-L1 \| base + temporal + label history [calibrated] | LogReg-L1 \| base + temporal [calibrated]    | roc_auc  |       0.070886   |   0.0410988   |    0.115866    |           0.0009995 |                1      |   20.7373  |   0.00341829 |   1.59746e-95  |                0.0089955 |    1.11822e-94  |
| LogReg-L1 \| base + temporal + label history [calibrated] | LogReg-L1 \| base + temporal [calibrated]    | f1       |       0.215752   |   0.161851    |    0.303203    |           0.0009995 |                1      |  nan       | nan          | nan            |                0.0089955 |  nan            |
| LogReg-L1 \| base + temporal + label history [calibrated] | LogReg-L1 \| base + temporal [calibrated]    | mcc      |       0.234889   |   0.172586    |    0.339119    |           0.0009995 |                1      |  nan       | nan          | nan            |                0.0089955 |  nan            |
| LogReg-L1 \| base + temporal + label history [calibrated] | LogReg-L1 \| label history only [calibrated] | pr_auc   |       0.19667    |   0.141803    |    0.243207    |           0.0029985 |                0.999  |  nan       | nan          | nan            |                0.017991  |  nan            |
| LogReg-L1 \| base + temporal + label history [calibrated] | LogReg-L1 \| label history only [calibrated] | roc_auc  |       0.101132   |   0.0427755   |    0.165515    |           0.0009995 |                1      |   23.7183  |   0.00426387 |   2.33485e-124 |                0.0089955 |    1.86788e-123 |
| LogReg-L1 \| base + temporal + label history [calibrated] | LogReg-L1 \| label history only [calibrated] | f1       |       0.0229939  |  -0.000235083 |    0.057271    |           0.055972  |                0.9725 |  nan       | nan          | nan            |                0.264868  |  nan            |
| LogReg-L1 \| base + temporal + label history [calibrated] | LogReg-L1 \| label history only [calibrated] | mcc      |       0.028051   |   0.00210359  |    0.0571084   |           0.0209895 |                0.99   |  nan       | nan          | nan            |                0.104948  |  nan            |
| LogReg-L1 \| base + temporal + label history [calibrated] | Persistence (label 14 steps earlier)        | pr_auc   |       0.216955   |   0.156158    |    0.277235    |           0.001999  |                0.9995 |  nan       | nan          | nan            |                0.015992  |  nan            |
| LogReg-L1 \| base + temporal + label history [calibrated] | Persistence (label 14 steps earlier)        | roc_auc  |       0.109881   |   0.0490349   |    0.177524    |           0.0009995 |                1      |   28.1083  |   0.00390921 |   7.75067e-174 |                0.0089955 |    6.9756e-173  |
| LogReg-L1 \| base + temporal + label history [calibrated] | Persistence (label 14 steps earlier)        | f1       |       0.0141262  |  -0.0180252   |    0.0542673   |           0.538731  |                0.731  |  nan       | nan          | nan            |                0.538731  |  nan            |
| LogReg-L1 \| base + temporal + label history [calibrated] | Persistence (label 14 steps earlier)        | mcc      |       0.0182759  |  -0.0122991   |    0.0511128   |           0.428786  |                0.786  |  nan       | nan          | nan            |                0.428786  |  nan            |

### 14.8 Block-length sensitivity (PR-AUC, B = 1000 per length)

|   block_length | model                                                                             | metric      |    ci_low |   ci_high |   ci_width |   p_block_bootstrap |
|---------------:|:----------------------------------------------------------------------------------|:------------|----------:|----------:|-----------:|--------------------:|
|              1 | LightGBM (baseline)                                                               | pr_auc      |  0.343811 |  0.417731 |   0.073919 |          nan        |
|              1 | LogReg-L1 (baseline)                                                              | pr_auc      |  0.339153 |  0.411362 |   0.072209 |          nan        |
|              1 | LogReg-L1 \| base + temporal [calibrated]                                          | pr_auc      |  0.391430 |  0.465211 |   0.073781 |          nan        |
|              1 | Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]                           | pr_auc      |  0.455614 |  0.529603 |   0.073989 |          nan        |
|              1 | LogReg-L1 \| base + temporal [calibrated] minus LightGBM (baseline)                | pr_auc_diff |  0.025520 |  0.071409 |   0.045889 |            0.001998 |
|              1 | LogReg-L1 \| base + temporal [calibrated] minus LogReg-L1 (baseline)               | pr_auc_diff |  0.034383 |  0.073896 |   0.039513 |            0.001998 |
|              1 | Ensemble (calibrated LightGBM + LogReg-L1) [calibrated] minus LightGBM (baseline) | pr_auc_diff |  0.089832 |  0.135320 |   0.045488 |            0.001998 |
|              7 | LightGBM (baseline)                                                               | pr_auc      |  0.292963 |  0.466853 |   0.173890 |          nan        |
|              7 | LogReg-L1 (baseline)                                                              | pr_auc      |  0.285993 |  0.458047 |   0.172054 |          nan        |
|              7 | LogReg-L1 \| base + temporal [calibrated]                                          | pr_auc      |  0.337275 |  0.509610 |   0.172335 |          nan        |
|              7 | Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]                           | pr_auc      |  0.402147 |  0.573738 |   0.171591 |          nan        |
|              7 | LogReg-L1 \| base + temporal [calibrated] minus LightGBM (baseline)                | pr_auc_diff |  0.008001 |  0.084774 |   0.076772 |            0.017982 |
|              7 | LogReg-L1 \| base + temporal [calibrated] minus LogReg-L1 (baseline)               | pr_auc_diff |  0.019765 |  0.085875 |   0.066111 |            0.009990 |
|              7 | Ensemble (calibrated LightGBM + LogReg-L1) [calibrated] minus LightGBM (baseline) | pr_auc_diff |  0.078951 |  0.149084 |   0.070133 |            0.001998 |
|             14 | LightGBM (baseline)                                                               | pr_auc      |  0.247848 |  0.490550 |   0.242702 |          nan        |
|             14 | LogReg-L1 (baseline)                                                              | pr_auc      |  0.247063 |  0.479433 |   0.232370 |          nan        |
|             14 | LogReg-L1 \| base + temporal [calibrated]                                          | pr_auc      |  0.286190 |  0.529846 |   0.243656 |          nan        |
|             14 | Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]                           | pr_auc      |  0.358969 |  0.596434 |   0.237465 |          nan        |
|             14 | LogReg-L1 \| base + temporal [calibrated] minus LightGBM (baseline)                | pr_auc_diff |  0.002240 |  0.088250 |   0.086010 |            0.047952 |
|             14 | LogReg-L1 \| base + temporal [calibrated] minus LogReg-L1 (baseline)               | pr_auc_diff |  0.010646 |  0.089105 |   0.078459 |            0.009990 |
|             14 | Ensemble (calibrated LightGBM + LogReg-L1) [calibrated] minus LightGBM (baseline) | pr_auc_diff |  0.072210 |  0.152637 |   0.080426 |            0.001998 |
|             28 | LightGBM (baseline)                                                               | pr_auc      |  0.207487 |  0.499325 |   0.291838 |          nan        |
|             28 | LogReg-L1 (baseline)                                                              | pr_auc      |  0.210645 |  0.488577 |   0.277932 |          nan        |
|             28 | LogReg-L1 \| base + temporal [calibrated]                                          | pr_auc      |  0.222433 |  0.533291 |   0.310857 |          nan        |
|             28 | Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]                           | pr_auc      |  0.310785 |  0.592538 |   0.281753 |          nan        |
|             28 | LogReg-L1 \| base + temporal [calibrated] minus LightGBM (baseline)                | pr_auc_diff | -0.008903 |  0.090369 |   0.099272 |            0.099900 |
|             28 | LogReg-L1 \| base + temporal [calibrated] minus LogReg-L1 (baseline)               | pr_auc_diff | -0.005919 |  0.088269 |   0.094188 |            0.063936 |
|             28 | Ensemble (calibrated LightGBM + LogReg-L1) [calibrated] minus LightGBM (baseline) | pr_auc_diff |  0.064775 |  0.152798 |   0.088023 |            0.007992 |
|             56 | LightGBM (baseline)                                                               | pr_auc      |  0.156204 |  0.507866 |   0.351661 |          nan        |
|             56 | LogReg-L1 (baseline)                                                              | pr_auc      |  0.157216 |  0.497127 |   0.339911 |          nan        |
|             56 | LogReg-L1 \| base + temporal [calibrated]                                          | pr_auc      |  0.183738 |  0.533129 |   0.349392 |          nan        |
|             56 | Ensemble (calibrated LightGBM + LogReg-L1) [calibrated]                           | pr_auc      |  0.256900 |  0.587938 |   0.331038 |          nan        |
|             56 | LogReg-L1 \| base + temporal [calibrated] minus LightGBM (baseline)                | pr_auc_diff | -0.004379 |  0.087117 |   0.091496 |            0.065934 |
|             56 | LogReg-L1 \| base + temporal [calibrated] minus LogReg-L1 (baseline)               | pr_auc_diff |  0.002161 |  0.087759 |   0.085598 |            0.051948 |
|             56 | Ensemble (calibrated LightGBM + LogReg-L1) [calibrated] minus LightGBM (baseline) | pr_auc_diff |  0.068249 |  0.145176 |   0.076927 |            0.009990 |
