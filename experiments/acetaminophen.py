from experiments import utility


def run_experiment():
      """
      Experiment: Paracetamol --> https://en.wikipedia.org/wiki/Paracetamol
      """
      context = """Paracetamol, also known as acetaminophen, is a medication used to treat fever and mild to moderate pain.[11][12] At a standard dose, paracetamol only slightly decreases body temperature;[11][13][14] it is inferior to ibuprofen in that respect,[15] and the benefits of its use for fever are unclear.[11][16][17] Paracetamol significantly relieves pain in acute migraine but only slightly in episodic tension headache.[18][19] However, the aspirin/paracetamol/caffeine combination helps with both conditions and is recommended as a first-line treatment for them.[20][21] Paracetamol is effective for post-surgical pain, but it is inferior to ibuprofen.[22] The paracetamol/ibuprofen combination provides further increase in potency and is superior to either drug alone.[22][23] The pain relief paracetamol provides in osteoarthritis is small and clinically insignificant.[12][24][25] The evidence in its favor for the use in low back pain, cancer pain and neuropathic pain is insufficient.[12][26][24][27][28][29]
      In the short term, common side effects of paracetamol are nausea and abdominal pain, and it seems to have tolerability similar to ibuprofen.[30][31] Chronic consumption of paracetamol may result in a drop in hemoglobin level indicating possible gastrointestinal bleeding[32] and abnormal liver function tests.[33] There is a consistent association of increased mortality as well as cardiovascular (stroke, myocardial infarction), gastrointestinal (ulcers, bleeding) and renal adverse effects with taking higher dose of paracetamol.[32][31][34] The drug may also increase the risk of developing hypertension.[35] Elevated frequency of asthma and developmental and reproductive disorders is observed in the offspring of women with prolonged use of paracetamol during pregnancy, although whether paracetamol is the true cause of this increase is unclear.[35] The evidence for the association between paracetamol during pregnancy and autism spectrum disorder and attention deficit hyperactivity disorder is particularly strong,[36][37] all this prompting the calls to limit its use in pregnancy to the lowest effective dosage for the shortest possible time.[35][38][39]
      The recommended maximum daily dose for an adult is three to four grams.[40][41][24] Higher doses may lead to toxicity, including liver failure.[42] Paracetamol poisoning is the foremost cause of acute liver failure in the Western world, and accounts for most drug overdoses in the United States, the United Kingdom, Australia, and New Zealand.[43][44][45]
      Paracetamol was first made in 1877 or possibly 1852.[46][47][48] It is the most commonly used medication for pain and fever in both the United States and Europe.[49] It is on the World Health Organization's List of Essential Medicines.[50] Paracetamol is available as a generic medication, with brand names including Tylenol and Panadol among others.[51] In 2018, it was the twentieth most commonly prescribed medication in the United States, with more than 27 million prescriptions.[52][53]"""

      question='What is acetaminophen?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))

      question='What are the side effects of acetaminophen?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))

      question='How much we should use acetaminophen per day?'
      print("Q: {} --> A: {}".format(question, utility.get_answer(question, 
            context)))