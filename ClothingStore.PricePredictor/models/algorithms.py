def create_algorithm(name: str):

    if name == "random_forest":
        from sklearn.ensemble import RandomForestRegressor

        return RandomForestRegressor(
            n_estimators=200,
            random_state=42,
            n_jobs=-1,
        )

    if name == "decision_tree":
        from sklearn.tree import DecisionTreeRegressor

        return DecisionTreeRegressor(
            random_state=42,
        )

    if name == "linear_regression":
        from sklearn.linear_model import LinearRegression

        return LinearRegression()

    if name == "cat_boost":
        from catboost import CatBoostRegressor

        return CatBoostRegressor(
            iterations=500,
            depth=6,
            learning_rate=0.1,
            loss_function="RMSE",
            random_seed=42,
            verbose=False,
        )

    raise ValueError(f"Unknown algorithm: {name}")