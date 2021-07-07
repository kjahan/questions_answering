from experiments import utility


def run_experiment():
      """
      Experiment: Covid-19 --> https://en.wikipedia.org/wiki/COVID-19
      """
      context = """Coronavirus disease 2019 (COVID-19) is a contagious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2). The first known case was identified in Wuhan, China in December 2019.[7] The disease has since spread worldwide, leading to an ongoing pandemic.[8]
      Symptoms of COVID-19 are variable, but often include fever,[9] cough, headache,[10] fatigue, breathing difficulties, and loss of smell and taste.[11][12][13] Symptoms may begin one to fourteen days after exposure to the virus. At least a third of people who are infected do not develop noticeable symptoms.[14] Of those people who develop noticeable symptoms enough to be classed as patients, most (81%) develop mild to moderate symptoms (up to mild pneumonia), while 14% develop severe symptoms (dyspnea, hypoxia, or more than 50% lung involvement on imaging), and 5% suffer critical symptoms (respiratory failure, shock, or multiorgan dysfunction).[15] Older people are at a higher risk of developing severe symptoms. Some people continue to experience a range of effects (long COVID) for months after recovery, and damage to organs has been observed.[16] Multi-year studies are underway to further investigate the long-term effects of the disease.[16]
      Transmission of COVID-19 occurs when people are exposed to virus-containing respiratory droplets and airborne particles exhaled by an infected person.[17][18] Those particles may be inhaled or may reach the mouth, nose, or eyes of a person through touching or direct deposition (i.e. being coughed on).[17] The risk of infection is highest when people are in close proximity for a long time, but particles can be inhaled over longer distances, particularly indoors in poorly ventilated and crowded spaces.[17][19] In those conditions small particles can remain suspended in the air for minutes to hours.[17] Touching a contaminated surface or object may lead to infection although this does not contribute substantially to transmission.[17][20] People who are infected can transmit the virus to another person up to two days before they themselves show symptoms, as can people who do not experience symptoms.[21][22] People remain infectious for up to ten days after the onset of symptoms in moderate cases and up to twenty days in severe cases.[23]
      Several testing methods have been developed to diagnose the disease. The standard diagnostic method is by detection of the virus' nucleic acid by real-time reverse transcription polymerase chain reaction (rRT-PCR), transcription-mediated amplification (TMA), or by reverse transcription loop-mediated isothermal amplification (RT-LAMP) from a nasopharyngeal swab.
      Preventive measures include physical or social distancing, quarantining, ventilation of indoor spaces, covering coughs and sneezes, hand washing, and keeping unwashed hands away from the face. The use of face masks or coverings has been recommended in public settings to minimize the risk of transmissions.
      While work is underway to develop drugs that inhibit the virus (and several vaccines for it have been approved and distributed in various countries, which have since initiated mass vaccination campaigns), the primary treatment is symptomatic. Management involves the treatment of symptoms, supportive care, isolation, and experimental measures."""

      question='What is Covid-19?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))

      question='What are Covid-19 symptoms?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))

      question='How fast Covid-19 spread?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))

      question='How to prevent Covid-19?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))

      question='Where does Covid-19 come from?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))

      question='What is Covid-19 treatment?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))

      question='What are Covid-19 tests?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))
