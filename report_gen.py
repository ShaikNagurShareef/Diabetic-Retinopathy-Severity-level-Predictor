from fpdf import FPDF
from datetime import date

def Generate_Report(name,gender,age,mobile,sc,Scale,scan):
	#create pdf object
	pdf = FPDF(orientation='P', unit='mm', format='A4') #orientation = ['P','L'], unit = ['mm','cm'], format = ['A3','A4','A5','letter','legal']

	#add a new page
	pdf.add_page()

	#set font to pdf object
	pdf.set_font("Arial",'B', size=16)
	pdf.set_text_color(255,0,0)
	
	#add logo as header
	img_path = 'logo.png'
	sp = "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
	title = 'Automated Diabetic Retinopathy Severity Identification'

	exs = 'Not Found'
	hms = 'Not Found'
	ma = 'Not Found'
	
	if(sc==0):
		dr = 'Negative'
	else:
		dr = 'Positive'

	if Scale==0:
		scale = 'None'
		ma='None'
		exs='None'
		hms='None'
	elif Scale==1:
		scale = 'Mild'
		ma = 'Present'
	elif Scale==2:
		scale = 'Moderate'
		ma = 'Present'
	elif Scale==3:
		scale = 'Severe'
		ma = 'Present'
		exs = 'Formed'
		hms = 'Found'
	else:
		scale = 'Proliferative'
		ma = 'Present'
		exs = 'Formed'
		hms = 'Found'




	pdf.image(img_path, x=80, y=8,w=60, h=20)
	pdf.ln(20)
        # Add Title
	pdf.cell(20)
	pdf.cell(20, 5, title, ln=1)
	pdf.ln(0.2)
	pdf.set_font("Arial", size=10)
	pdf.set_text_color(0,0,0)
	pdf.cell(0, 5, 'Date: %s' % date.today().strftime("%b-%d-%Y"), ln=0)
	pdf.cell(0, 5, "Shaik Nagur Shareef (+91 8309913300)",align="R", ln=1)
	#draw line
	pdf.set_line_width(0.5)
	pdf.line(10, 40, 200, 40)
	pdf.ln(2)

	pdf.set_font("Arial",'B', size=12)
	pdf.set_text_color(0,0,255)

	pdf.cell(0, 5, "Patient Details",align="C", ln=1)
        
	pdf.set_font("Arial", size=12)
	pdf.set_text_color(0,0,0)

	pdf.ln(5)
	pdf.cell(0, 5, "Name    :"+sp+sp+sp+name ,align="L", ln=1)
	pdf.ln(2)
	pdf.cell(0, 5, "Gender  :"+sp+sp+sp+gender ,align="L", ln=1)
	pdf.ln(2)
	pdf.cell(0, 5, "Age     \t\t:"+sp+sp+sp+str(age)+" years" ,align="L", ln=1)
	pdf.ln(2)
	pdf.cell(0, 5, "Mobile \t\t:"+sp+sp+sp+str(mobile) ,align="L", ln=1)
	pdf.ln(5)
	pdf.set_font("Arial",'B', size=12)
	pdf.set_text_color(0,0,255)

	pdf.cell(0, 5, "Diagonosis Report",align="C", ln=1)
        

	pdf.set_font("Arial", size=12)
	pdf.set_text_color(0,0,0)

	pdf.ln(5)
	pdf.cell(0, 5, "Diabetic Retinopathy    :"+sp+sp+dr ,align="L", ln=1)
	pdf.ln(2)
	pdf.cell(0, 5, "Severity                \t\t\t\t\t\t\t\t:"+sp+sp+scale ,align="L", ln=1)
	pdf.ln(2)
	pdf.cell(0, 5, "Micro Aneurysms		 \t\t\t\t\t\t:"+sp+sp+ma ,align="L", ln=1)
	pdf.ln(2)
	pdf.cell(0, 5, "Hemorrhages             \t\t:"+sp+sp+hms ,align="L", ln=1)
	pdf.ln(2)
	pdf.cell(0, 5, "Exudates                \t\t\t\t\t\t:"+sp+sp+exs ,align="L", ln=1)

	pdf.ln(10)

	#add Scan
	pdf.image(scan, x=40, y=140,w=128, h=128)

	# save file
	pdf.output("static/Reports/"+name+".pdf")
