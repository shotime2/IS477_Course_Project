rule run_all:
    input:
        "merged/merged_ev_and_air.csv",
        "analysis/correlation_table.csv",
        "analysis/PM25_scatterplot.png",
        "analysis/Ozone_scatterplot.png"

rule clean_ev_data:
    input:
        "raw/ev_raw.csv"
    output:
        "clean/ev_state_year_clean.csv"
    shell:
        "python scripts/ev_clean.py"

rule fetch_air_data:
    input:
        "raw/raw_air_quality.csv"
    output:
        "clean/air_state_year_clean.csv"
    shell:
        "python scripts/fetch_air_data.py && python scripts/air_data_clean.py"

rule merge_data:
    input:
        ev="clean/ev_state_year_clean.csv",
        air="clean/air_state_year_clean.csv"
    output:
        "merged/merged_ev_and_air.csv"
    shell:
        "python scripts/merge.py"

rule analysis:
    input:
        "merged/merged_ev_and_air.csv"
    output:
        "analysis/correlation_table.csv",
        "analysis/PM25_scatterplot.png",
        "analysis/Ozone_scatterplot.png"
    shell:
        "python scripts/Analysis.py"
