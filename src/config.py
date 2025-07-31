from datetime import date

DATABASE_METADATA = {
  1: {
    "database_id": 1,
    "country": "Canada",
    "dataset_name": "SARS-CoV-2 antibody seroprevalence in Canadians, by age group and sex, November 2020 to April 2021",
    "description": "[Subsetted to only include national-level data] Seroprevalence of Canadians aged 1 and older with antibodies against SARS-CoV-2 (the virus that causes COVID-19), overall and by antibody type, by age group and sex.",
    "last_updated": "2025-05-26"
  },
  2: {
    "database_id": 2,
    "country": "Canada",
    "dataset_name": "COVID-19 Rapid Test kits demand and usage",
    "description": "[Subsetted to only include national-level data] Percent of businesses that used COVID-19 Rapid Test kits to test on-site employees and percent of businesses that plan to test on-site employees in the next threee months by North American Industry Classification System (NAICS) for Canada and regions. Includes business' reason for not having plans to use COVID-19 Rapid Test Kits in the next three months and the percent of businesses that test employees less than once a week/once a week/twice a week/more than twice a week. Further includes percent of businesses that indicated COVID-19 Rapid Test kits as being essential personal protective equipment (PPE) or that expect to have shortages within the next 3 months.",
    "last_updated": "2025-05-26"
  },
  3: {
    "database_id": 3,
    "country": "United Kingdom (UK)",
    "dataset_name": "Covid-19 Cases By Day",
    "description": "National count of new Covid-19 cases in the United Kingdom. Includes epidemiological week.",
    "last_updated": str(date.today())
  },
  4: {
    "database_id": 4,
    "country": "United States of America (USA)",
    "dataset_name": "Provisional COVID-19 death counts and rates by month, jurisdiction of residence, and demographic characteristics",
    "description": """[Subsetted to only include national-level data] This file contains COVID-19 death counts and rates by month and year of death, jurisdiction of residence (U.S., HHS Region) and demographic characteristics (sex, age, race and Hispanic origin, and age/race and Hispanic origin). United States death counts and rates include the 50 states, plus the District of Columbia.

Deaths with confirmed or presumed COVID-19, coded to ICD–10 code U07.1. Number of deaths reported in this file are the total number of COVID-19 deaths received and coded as of the date of analysis and may not represent all deaths that occurred in that period. Counts of deaths occurring before or after the reporting period are not included in the file.

Data during recent periods are incomplete because of the lag in time between when the death occurred and when the death certificate is completed, submitted to NCHS and processed for reporting purposes. This delay can range from 1 week to 8 weeks or more, depending on the jurisdiction and cause of death.

Death counts should not be compared across jurisdictions. Data timeliness varies by state. Some states report deaths on a daily basis, while other states report deaths weekly or monthly.

Rates were calculated using the population estimates for 2021, which are estimated as of July 1, 2021 based on the Blended Base produced by the US Census Bureau in lieu of the April 1, 2020 decennial population count. The Blended Base consists of the blend of Vintage 2020 postcensal population estimates, 2020 Demographic Analysis Estimates, and 2020 Census PL 94-171 Redistricting File (see https://www2.census.gov/programs-surveys/popest/technical-documentation/methodology/2020-2021/methods-statement-v2021.pdf).

Rate are based on deaths occurring in the specified week and are age-adjusted to the 2000 standard population using the direct method (see https://www.cdc.gov/nchs/data/nvsr/nvsr70/nvsr70-08-508.pdf). These rates differ from annual age-adjusted rates, typically presented in NCHS publications based on a full year of data and annualized weekly age-adjusted rates which have been adjusted to allow comparison with annual rates. Annualization rates presents deaths per year per 100,000 population that would be expected in a year if the observed period specific (weekly) rate prevailed for a full year.""",
    "last_updated": str(date.today())
  }
}
