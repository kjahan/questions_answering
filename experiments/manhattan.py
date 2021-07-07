from experiments import utility


def run_experiment():
      """
      Experiment: Manhattan Project --> https://en.wikipedia.org/wiki/Manhattan_Project
      """
      guardian_context="""The Manhattan Project was a research and development undertaking during 
      World War II that produced the first nuclear weapons. It was led by the United States with the 
      support of the United Kingdom (which initiated the original Tube Alloys project) and Canada. 
      From 1942 to 1946, the project was under the direction of Major General Leslie Groves of the 
      U.S. Army Corps of Engineers. Nuclear physicist Robert Oppenheimer was the director of the 
      Los Alamos Laboratory that designed the actual bombs. As engineer districts by convention 
      carried the name of the city where they were located, the Army component of the project was 
      designated the Manhattan District; Manhattan gradually superseded the official codename, 
      Development of Substitute Materials, for the entire project. Along the way, the project absorbed 
      its earlier British counterpart, Tube Alloys. The Manhattan Project began modestly in 1939, 
      but grew to employ more than 130,000 people and cost nearly US$2 billion (equivalent to about 
      $23 billion in 2019).[1] Over 90 percent of the cost was for building factories and to 
      produce fissile material, with less than 10 percent for development and production of the weapons. 
      Research and production took place at more than thirty sites across the United States, the 
      United Kingdom, and Canada. Two types of atomic bombs were developed concurrently during the 
      war: a relatively simple gun-type fission weapon and a more complex implosion-type nuclear 
      weapon. The Thin Man gun-type design proved impractical to use with plutonium, and therefore a 
      simpler gun-type called Little Boy was developed that used uranium-235, an isotope that makes 
      up only 0.7 percent of natural uranium. Since it was chemically identical to the most common 
      isotope, uranium-238, and had almost the same mass, separating the two proved difficult. Three 
      methods were employed for uranium enrichment: electromagnetic, gaseous and thermal. Most of 
      this work was performed at the Clinton Engineer Works at Oak Ridge, Tennessee. 
      In parallel with the work on uranium was an effort to produce plutonium, which was discovered 
      by researchers at the University of California, Berkeley, in 1940. After the feasibility of the 
      world's first artificial nuclear reactor, the Chicago Pile-1, was demonstrated in 1942 at the 
      Metallurgical Laboratory in the University of Chicago, the Project designed the X-10 Graphite 
      Reactor at Oak Ridge and the production reactors at the Hanford Site in Washington state, in 
      which uranium was irradiated and transmuted into plutonium. The plutonium was then chemically 
      separated from the uranium, using the bismuth phosphate process. The Fat Man plutonium 
      implosion-type weapon was developed in a concerted design and development effort by the Los 
      Alamos Laboratory. The project was also charged with gathering intelligence on the German 
      nuclear weapon project. Through Operation Alsos, Manhattan Project personnel served in Europe, 
      sometimes behind enemy lines, where they gathered nuclear materials and documents, and rounded 
      up German scientists. Despite the Manhattan Project's tight security, Soviet atomic spies 
      successfully penetrated the program. The first nuclear device ever detonated was an 
      implosion-type bomb at the Trinity test, conducted at New Mexico's Alamogordo Bombing and 
      Gunnery Range on 16 July 1945. Little Boy and Fat Man bombs were used a month later in the 
      atomic bombings of Hiroshima and Nagasaki, respectively, with Manhattan Project personnel 
      serving as bomb assembly technicians, and as weaponeers on the attack aircraft. In the 
      immediate postwar years, the Manhattan Project conducted weapons testing at Bikini Atoll as 
      part of Operation Crossroads, developed new weapons, promoted the development of the network 
      of national laboratories, supported medical research into radiology and laid the foundations 
      for the nuclear navy. It maintained control over American atomic weapons research and production 
      until the formation of the United States Atomic Energy Commission in January 1947."""

      question='When was Manhattan Project?'
      print("question: {} --> answer: {}".format(question, utility.get_answer(question, 
            guardian_context)))

      question='What was Manhattan Project?'
      print("question: {} --> answer: {}".format(question, utility.get_answer(question, 
            guardian_context)))

      question='How many people worked on Manhattan Project?'
      print("question: {} --> answer: {}".format(question, utility.get_answer(question, 
            guardian_context)))

      question='How much Manhattan Project costed?'
      print("question: {} --> answer: {}".format(question, utility.get_answer(question, 
            guardian_context)))
