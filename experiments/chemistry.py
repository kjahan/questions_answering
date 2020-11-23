from experiments import utility


def run_oxygen_experiment():
	"""
	Experiment I: Oxygen --> https://en.wikipedia.org/wiki/Triangle
	"""
	oxygen_context="Oxygen is the chemical element with the symbol O and atomic number 8. It is a member of the \
						chalcogen group in the periodic table, a highly reactive nonmetal, and an oxidizing agent \
						that readily forms oxides with most elements as well as with other compounds. After hydrogen \
						and helium, oxygen is the third-most abundant element in the universe by mass. At standard \
						temperature and pressure, two atoms of the element bind to form dioxygen, a colorless and \
						odorless diatomic gas with the formula O2. Diatomic oxygen gas constitutes 20.95 percent of \
						the Earth's atmosphere. Oxygen makes up almost half of the Earth's crust in the form of oxides."

	question_1="What is the Oxygen symbol?"
	print("question #1: {} --> answer: {}".format(question_1, utility.get_answer(question_1, oxygen_context)))

	question_2="What is the atomic number of Oxygen?"
	print("question #2: {} --> answer: {}".format(question_2, utility.get_answer(question_2, oxygen_context)))

	question_3="What is the first-most abundant element in the universe?"
	print("question #3: {} --> answer: {}".format(question_3, utility.get_answer(question_3, oxygen_context)))


def run_morphine_experiment():
	"""
	Experiment II: Morphine --> https://en.wikipedia.org/wiki/Morphine
	"""
	morphine_context="Morphine is a pain medication of the opiate family that is found naturally in a number of \
					plants and animals, including humans. It acts directly on the central nervous system \
					(CNS) to decrease the feeling of pain. It can be taken for both acute pain and chronic \
					pain and is frequently used for pain from myocardial infarction and during labor. Morphine \
					can be administered by mouth, by injection into a muscle, by injection under the skin, intravenously, \
					injection into the space around the spinal cord, or rectally. Its maximum effect is reached \
					after about 20 minutes when administered intravenously and 60 minutes when administered by \
					mouth, while the duration of its effect is 3–7 hours. Long-acting formulations of morphine \
					also exist. Potentially serious side effects of morphine include decreased respiratory effort \
					and low blood pressure. Morphine is addictive and prone to abuse. If one's dose is reduced \
					after long-term use, opioid withdrawal symptoms may occur. Common side effects of morphine \
					include drowsiness, vomiting, and constipation. Caution is advised for use of morphine during \
					pregnancy or breast feeding, as it may affect the health of the baby. Morphine was first isolated \
					between 1803 and 1805 by German pharmacist Friedrich Sertürner. This is generally believed to \
					be the first isolation of an active ingredient from a plant. Merck began marketing it \
					commercially in 1827. Morphine was more widely used after the invention of the hypodermic \
					syringe in 1853–1855. Sertürner originally named the substance morphium, after the Greek god of \
					dreams, Morpheus, as it has a tendency to cause sleep. The primary source of morphine is \
					isolation from poppy straw of the opium poppy. In 2013, approximately 523 tons of morphine \
					were produced. Approximately 45 tons were used directly for pain, a four-fold increase over the \
					last twenty years. Most use for this purpose was in the developed world. About 70 percent \
					of morphine is used to make other opioids such as hydromorphone, oxymorphone, and heroin. \
					It is a Schedule II drug in the United States, Class A in the United Kingdom, and Schedule I \
					in Canada. It is also on the World Health Organization's List of Essential Medicines. \
					Morphine is sold under many trade names. In 2017, it was the 155th-most commonly prescribed \
					medication in the United States, with more than four million prescriptions."

	question_1="What is Morphone?"
	print("question #1: {} --> answer: {}".format(question_1, utility.get_answer(question_1, morphine_context)))

	question_2="What is the use of Morphine?"
	print("question #2: {} --> answer: {}".format(question_2, utility.get_answer(question_2, morphine_context)))

	question_3="What are the side effects of Morphine?"
	print("question #3: {} --> answer: {}".format(question_3, utility.get_answer(question_3, morphine_context)))
