import streamlit as s
s.bg="""
<style>
s.stapp {
     background-image: image("Screenshot 2025-04-24 123117.png")
     }
     </style>
     """
s.title("bmi calculator")
h=0.00
w=0
w = s.number_input(f"please type your weight",min_value=1.00,max_value=500.00) 
h = s.number_input(f"now please put your height (cm)",step=0.1,min_value=1.00,max_value=450.00)
bmi=w/(h/100)**2
if bmi<18.5:
    s.info(f"{bmi}")
    s.info("underweight")
    s.warning("You're so skinny, when you turn sideways, you disappeared.")
    s.image("skinny.png.png")
elif bmi<23:
    s.info(f"{bmi}")
    s.info("healthy")
    s.success("keep up")
    s.image("normal.png")
elif bmi<25:
    s.info(f"{bmi}")
    s.info("overweight")
    s.warning("diet please?")
    s.image("chubby walter.png")
elif bmi<30:
    s.info(f"{bmi}")
    s.info("fat")
    s.error("you make a sumo wrestler look like a supermodel")
    s.image("brainrot have skibidi rizz.png")
else:
    s.info(f"{bmi}")
    s.info("very fat... infact,u r caseoh reincarnate")
    s.error("You're an absolute gluttonous beast, and the only exercise you get is lifting a fork to your mouth,People mistake you for a planet because of the gravitational pull you have on their food,You're the reason they invented double doors!,You're so fat the only letters of the alphabet you know are KFC.")
    s.image("caseoh.png")
