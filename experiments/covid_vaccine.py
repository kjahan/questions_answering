from experiments import utility


def run_experiment():
      """
      Experiment: Covid-19 vaccine --> https://en.wikipedia.org/wiki/COVID-19_vaccine
      """
      context = """A COVID‑19 vaccine is a vaccine intended to provide acquired immunity against severe acute respiratory syndrome coronavirus 2 (SARS‑CoV‑2), the virus that causes coronavirus disease 2019 (COVID‑19). Prior to the COVID‑19 pandemic, an established body of knowledge existed about the structure and function of coronaviruses causing diseases like severe acute respiratory syndrome (SARS) and Middle East respiratory syndrome (MERS). This knowledge accelerated the development of various vaccine technologies during early 2020.[1] On 10 January 2020, the SARS-CoV-2 genetic sequence data was shared through GISAID, and by 19 March, the global pharmaceutical industry announced a major commitment to address COVID-19.[2] The COVID‑19 vaccines are widely credited for their role in reducing the spread, severity, and death caused by COVID-19.[3]
      In Phase III trials, several COVID‑19 vaccines have demonstrated efficacy as high as 95% in preventing symptomatic COVID‑19 infections. As of June 2021, 19 vaccines are authorized by at least one national regulatory authority for public use: two RNA vaccines (Pfizer–BioNTech and Moderna), nine conventional inactivated vaccines (BBIBP-CorV, Chinese Academy of Medical Sciences, CoronaVac, Covaxin, CoviVac, COVIran Barakat, Minhai-Kangtai, QazVac, and WIBP-CorV), five viral vector vaccines (Sputnik Light, Sputnik V, Oxford–AstraZeneca, Convidecia, and Johnson & Johnson), and three protein subunit vaccines (EpiVacCorona, Soberana 02, and RBD-Dimer).[4][failed verification] In total, as of March 2021, 308 vaccine candidates are in various stages of development, with 73 in clinical research, including 24 in Phase I trials, 33 in Phase I–II trials, and 16 in Phase III development.[4]
      Many countries have implemented phased distribution plans that prioritize those at highest risk of complications, such as the elderly, and those at high risk of exposure and transmission, such as healthcare workers.[5] Single dose interim use is under consideration to extend vaccination to as many people as possible until vaccine availability improves.[6][7][8][9]
      As of 3 July 2021, 3.19 billion doses of COVID‑19 vaccine have been administered worldwide based on official reports from national health agencies.[10] AstraZeneca anticipates producing 3 billion doses in 2021, Pfizer–BioNTech 1.3 billion doses, and Sputnik V, Sinopharm, Sinovac, and Johnson & Johnson 1 billion doses each. Moderna targets producing 600 million doses and Convidecia 500 million doses in 2021.[11][12] By December 2020, more than 10 billion vaccine doses had been preordered by countries,[13] with about half of the doses purchased by high-income countries comprising 14% of the world's population.[14]"""

      question='What are the types of Covid-19 vaccines?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))

      question='What are RNA vaccines?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))

      question='How many people have been vaccinated so far?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))
