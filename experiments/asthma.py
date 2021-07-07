from experiments import utility


def run_experiment():
      """
      Experiment: Asthma --> https://en.wikipedia.org/wiki/Asthma
      """
      context = """Asthma is a long-term inflammatory disease of the airways of the lungs.[3] It is characterized by variable and recurring symptoms, reversible airflow obstruction, and easily triggered bronchospasms.[10][11] Symptoms include episodes of wheezing, coughing, chest tightness, and shortness of breath.[2] These may occur a few times a day or a few times per week.[3] Depending on the person, asthma symptoms may become worse at night or with exercise.[3]
      Asthma is thought to be caused by a combination of genetic and environmental factors.[4] Environmental factors include exposure to air pollution and allergens.[3] Other potential triggers include medications such as aspirin and beta blockers.[3] Diagnosis is usually based on the pattern of symptoms, response to therapy over time, and spirometry lung function testing.[5] Asthma is classified according to the frequency of symptoms, forced expiratory volume in one second (FEV1), and peak expiratory flow rate.[12] It may also be classified as atopic or non-atopic, where atopy refers to a predisposition toward developing a type 1 hypersensitivity reaction.[13][14]
      There is no known cure for asthma, but it is easily treatable.[3] Symptoms can be prevented by avoiding triggers, such as allergens and respiratory irritants, and suppressed with the use of inhaled corticosteroids.[6][15] Long-acting beta agonists (LABA) or antileukotriene agents may be used in addition to inhaled corticosteroids if asthma symptoms remain uncontrolled.[16][17] Treatment of rapidly worsening symptoms is usually with an inhaled short-acting beta-2 agonist such as salbutamol and corticosteroids taken by mouth.[7] In very severe cases, intravenous corticosteroids, magnesium sulfate, and hospitalization may be required.[18]
      In 2015, 358 million people globally had asthma, up from 183 million in 1990.[8][19] It caused about 397,100 deaths in 2015,[9] most of which occurred in the developing world.[3] Asthma often begins in childhood,[3] and the rates have increased significantly since the 1960s.[20] Asthma was recognized as early as Ancient Egypt.[21] The word "asthma" is from the Greek ἅσθμα, ásthma, which means "panting".[22]"""

      question='What is Asthma?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))

      question='What are the symptoms of Asthma?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))

      question='How can you treat Asthma?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))

      question='What causes Asthma?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))
