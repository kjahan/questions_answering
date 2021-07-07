from experiments import utility


def run_experiment():
      """
      Experiment: Guardian of Galaxy --> https://en.wikipedia.org/wiki/Guardians_of_the_Galaxy_(film)
      """
      guardian_context="""Guardians of the Galaxy (retroactively referred to as Guardians of the 
            Galaxy Vol. 1) is a 2014 American superhero film based on the Marvel Comics superhero 
            team of the same name. Produced by Marvel Studios and distributed by Walt Disney Studios 
            Motion Pictures, it is the 10th film in the Marvel Cinematic Universe (MCU). Directed by 
            James Gunn, who wrote the screenplay with Nicole Perlman, the film features an ensemble 
            cast including Chris Pratt, Zoe Saldana, Dave Bautista, Vin Diesel, and Bradley Cooper as 
            the titular Guardians, along with Lee Pace, Michael Rooker, Karen Gillan, Djimon Hounsou, 
            John C. Reilly, Glenn Close, and Benicio del Toro. In the film, Peter Quill and a group of 
            extraterrestrial criminals go on the run after stealing a powerful artifact. Perlman began 
            working on the screenplay in 2009. Producer Kevin Feige first publicly mentioned Guardians 
            of the Galaxy as a potential film in 2010 and Marvel Studios announced it was in active 
            development at the July 2012 San Diego Comic-Con. Gunn was hired to write and direct the 
            film that September. In February 2013, Pratt was hired to play Peter Quill / Star-Lord, 
            and the supporting cast members were subsequently confirmed. Principal photography began 
            in July 2013 at Shepperton Studios in England, with filming continuing in London before 
            wrapping up in October 2013. In addition to an original score by Tyler Bates, the film's 
            soundtrack includes several popular songs from the 1960s and 1970s chosen by Gunn. 
            Post-production was completed on July 7, 2014. Guardians of the Galaxy premiered at the 
            Dolby Theatre in Hollywood on July 21, 2014, and was theatrically released in the United 
            States on August 1, as part of Phase Two of the MCU. The film became a critical and 
            commercial success, grossing $772.8 million worldwide and becoming the highest-grossing 
            superhero film of 2014, as well as the third-highest-grossing film of 2014. The film was 
            praised for its screenplay, direction, acting, humor, soundtrack, visual effects, and action 
            sequences. At the 87th Academy Awards, the film received nominations for Best Visual Effects 
            and Best Makeup and Hairstyling, and also won the Hugo Award for Best Dramatic Presentation 
            in 2015. The sequel, Guardians of the Galaxy Vol. 2, was released in 2017. The third film, 
            Guardians of the Galaxy Vol. 3, will be released in 2023."""

      question='When did Gaurdian of Galaxy was made?'
      print("question: {} --> answer: {}".format(question, utility.get_answer(question, 
            guardian_context)))

      question='How much was the movie budget?'
      print("question: {} --> answer: {}".format(question, utility.get_answer(question, 
            guardian_context)))

      question='How much was the movie revenue?'
      print("question: {} --> answer: {}".format(question, utility.get_answer(question, 
            guardian_context)))

      question='What studio made the Guardian of Galaxy?'
      print("question: {} --> answer: {}".format(question, utility.get_answer(question, 
            guardian_context)))

      question='What awards did the Guardian of Galaxy win?'
      print("question: {} --> answer: {}".format(question, utility.get_answer(question, 
            guardian_context)))
