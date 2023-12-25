import openai
from openai import OpenAI

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))
import os 

# Set your API key

# Function to send a prompt to GPT-4 and receive a response
def get_input(prompt, info, model="gpt-4-1106-preview", max_tokens=4096):
    try:
        response = client.chat.completions.create(model=model,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": info}
        ],
        max_tokens=max_tokens)
        return response.choices[0].message.content
    except openai.OpenAIError as e:
        print(f"An error occurred: {e}")
        return None

# Embedded document contents (replace these placeholders with actual contents of your documents)
msu_plan_contents = """MSU Sustainabiltiy Plan:
Stewardship and Sustainability
Michigan State is working toward climate neutrality by mid-century, doing our part to address the global climate crisis within our own community and on our own campus. On this journey, we aim to reduce greenhouse gas emissions by 50% from our 2010 baseline, eliminating 292,934 metric tons of CO2.

To achieve our vision, we will be good stewards of resources and pursue initiatives in a manner that ensures our long-term sustainability and success. As we move into the next decade, with heightened competition for resources, declining federal and state support and concern about the cost of higher education, we must make focused and strategic use of our resources. We have a responsibility to use operational practices that reflect sound stewardship, efficiency and sustainability, while affirming that those efforts should not compromise the quality, safety or accessibility of our operations. We acknowledge also that we must do all we can within our means to deliver positive, supportive, engaging and enriching living, working, learning and recreational environments and experiences that our students, faculty and staff require to thrive and succeed and to continue to make MSU an attractive choice.

Our size and scope of activity are great strengths, but they can create operational silos that become barriers to the most effective deployment of resources. While respecting unique programmatic needs, we will leverage our collective institutional resources to support cross-institutional initiatives that advance our strategic priorities; reduce barriers to operational efficiency; and align the university’s fiscal, physical, technological and human resources to support our pursuit of excellence, advance equity and amplify our impact.

Read more...
Goal: Provide exemplary stewardship of institutional resources to foster the long-term sustainability of MSU and its high-quality education, research and outreach and engagement programs

Objective 1
Develop and implement a long-term, comprehensive financial model and budget process that aligns resources with strategic priorities; ensures university-wide effectiveness and efficiency; and sustains, expands and diversifies revenue sources

Strategies/Actions

Transform the university’s budgeting process using an “all funds” approach to provide a financial management framework to support strategic priorities. Create and use unit-level financial dashboards that provide up-to-date data to support strategic decision-making
Increase private support and launch the next comprehensive Capital Campaign
Review and update the Spartan Athletics strategic plan in the context of the significant national evolution of collegiate athletics
Pursue significant strategic external partnerships that support our mission, align with our values and expand our reach
Integrate and streamline administrative systems and processes to gain efficiencies and improve the user experience
Ensure ongoing examination of the portfolio of academic programs to best meet the evolving needs of prospective students and employers, expand our reach and diversify our student population
Objective 2
Create a new University Comprehensive Facilities and Land Use Plan that embeds diversity, equity and inclusion; faculty, staff and student success; and sustainable health in the physical environment of MSU’s campuses and facilities

Strategies/Actions

Incorporate multiple perspectives into the planning process including consideration of the history of the land MSU occupies, tribal consultation around archeological sites and environmental impact reviews
Ensure faculty, staff and students can live, work and learn in buildings and spaces that promote health and wellness, including incorporation of WELL building practices, proximal green space and pedestrian and bicycle-friendly design
Coordinate and integrate with frameworks and plans for utilities, mobility and preservation and management of open spaces
Incorporate campus “district” plans including collaboration/innovation zones throughout campus
Plan for and construct/renovate high-priority facilities that support the MSU articulated priorities and values (e.g., multicultural center, recreational sports facilities, greenhouses, engineering facility)
Ensure wayfinding is accessible for all users
Enhance public art on campus and ensure it includes multiple modalities and diverse perspectives
Objective 3
Achieve climate neutrality by 2050 through technology innovation, fiscal stewardship and embedding sustainability into institutional culture

Strategies/Actions

Develop an institutional Sustainability and Climate Action Plan using a four-pillar framework focused on: Campus, Curriculum, Community and Culture
Foster resource stewardship through application of Leadership in Environmental Design (LEED) principles, organically managed land, reducing greenhouse gas emissions, increasing sustainable source purchases, increasing campus-grown and/or locally sourced food and reducing transportation carbon footprint
Expand sustainability teaching and learning opportunities through formal courses and co-curricular activities
Expand sustainability research and innovation through inter- and intra-institution partnerships to address climate solutions
Enhance sustainability outreach and engagement by expanding volunteer opportunities for faculty, staff and students in support of local, state, regional, national and global partnerships
Objective 4
Develop a Sustainable Information Technology (IT) Strategic Plan to power the academic enterprise, Spartan innovation and sustainable business operations through enhanced access to information, operational technologies and strategic infrastructure

Strategies/Actions

Improve and enhance IT services and infrastructure to improve access and reliability, and enable greater avenues for innovation in teaching, research and scholarly activity
Expand access to technologies such as artificial intelligence, machine learning and augmented and virtual reality to enhance learning, research, community engagement and MSU’s reach
Provide operational excellence by leveraging technology to provide informed decision-making, reduce operating costs and optimize the capabilities of our teams
Objective 5
Ensure faculty, staff, students and community members have access to MSU and its resources to address current and emerging issues that affect Michigan and the world

Strategies/Actions

Ensure faculty, staff and students have the tools and network connectivity needed to succeed in remote, virtual and/or hybrid modalities
Increase access for persons with disabilities
Expand learning and applied learning opportunities through programs like micro-internships and stackable certificates
Establish reciprocal opportunities for partnering with businesses and community organizations to enhance each other’s work
In partnership with Detroit stakeholders, identify and implement a strategic framework to guide education, scholarly and outreach activities in Detroit to promote advancement of social and economic impacts in the state’s largest city
Stewardship and Sustainability: Illustrative Indicators/Metrics
View Illustrative Metrics
By 2030, reduce greenhouse gas emissions by 50% from 2010 baseline (cut by 292,934 metric tons of CO2)
By July 1, 2022, develop clear guidelines that align resources with strategic priorities
Increase nontuition and nonstate appropriations revenue by 20% by 2026
Complete the University Comprehensive Facilities and Land Use Plan by the end of 2022
Achieve platinum ranking in the Sustainability Tracking Assessment and Rating System (STARS) by 2030
Achieve top 100 Times Higher Education Global Impact ranking by 2030
Enterprise-level resources from the SMART campus technologies sector (increase)
Colleges with outreach and engagement and engaged scholarship integrated into college unit missions and strategic plans (100% by 2025)
    """
jesuit_principles_contents = """Jesuit Apostolic Preferences Letter:
To collaborate in the care of our Common Home



In the encyclical Laudato Si’, Pope Francis reminds us that all human beings share
responsibility for care of creation, considered by many peoples “mother earth.” “This sister now
cries out to us because of the harm we have inflicted on her by our irresponsible use and abuse
of the goods with which God has endowed her. (...) This is why the earth herself, burdened and
laid waste, is among the most abandoned and maltreated of our poor; she ‘groans in travail’”
(Rom 8:22).7



The damage done to the earth is also damage done to the most vulnerable, such as indigenous
peoples, peasants forced to emigrate, and the inhabitants of urban peripheries. The
environmental destruction being caused by the dominant economic system is inflicting
intergenerational damage: not only does it affect those now living on earth, particularly the very
young, but it also conditions and jeopardizes the life of future generations.



We resolve, considering who we are and the means that we have, to collaborate with others
in the construction of alternative models of life that are based on respect for creation and
on a sustainable development capable of producing goods that, when justly distributed,
ensure a decent life for all human beings on our planet. The preservation over time of the
conditions of life on our planet is a human responsibility of immense ethical and spiritual
importance. Our collaboration should include both participating in efforts to analyze problems
in depth and promoting reflection and discernment that will guide us in making decisions that
help to heal the wounds already inflicted on the delicate ecological balance. We are especially
concerned about areas that are so crucial for maintaining the natural equilibrium that makes life
possible, such as the Amazon region; the river basins of the Congo, India, and Indonesia; and
the great extensions of open sea. Caring for nature in this way is a form of genuinely
worshipping the creative work of God. Bold decisions are required to avoid further damage and
to bring about lifestyle changes that are necessary so that the goods of creation are used for the
benefit of all. We want to be actively present in this process.



Laudato Si’ reminds us that “disinterested concern for others, and the rejection of every form
of self-centeredness and self-absorption, are essential if we truly wish to care for our brothers
7 Laudato Si’, 2.



6



and sisters and for the natural environment. These attitudes also attune us to the moral
imperative of assessing the impact of our every action and personal decision on the world
around us.”8 It is logical to conclude that what Christians “need is an ‘ecological conversion,’
whereby the effects of their encounter with Jesus Christ become evident in their relationship
with the world around them. Living our vocation to be protectors of God’s handiwork is
essential to a life of virtue.”9



It is necessary, therefore, to step out of oneself and lovingly care for everything that is good
for others. A model of human life reconciled with creation will not be possible if we are not
able to break out of individualism and inaction.



Conversion for us, Jesuits and our companions in mission, begins by changing the habits of
life promoted by an economic and cultural system based on the consumption of an irrational
production of goods. The words of Pope Francis encourage us in this direction: "There is a
nobility in the duty to care for creation through little daily actions, and it is wonderful how
education can bring about real changes in lifestyle


"""
foundational_document_contents = """Foundational Concepts for SJU Centers and Institutes Strategy:
The governing principles of the Society of Jesus, also known as the Jesuits, are:
Cura personalis: Care for the individual person. This principle is reflected in the Jesuit commitment to helping each person grow in their relationship with God and to become a more fully realized human being.
Cura apostolica: Care for the apostolic mission. This principle is reflected in the Jesuit commitment to work for the greater glory of God and the good of all humanity.
Unity of heart, mind, and soul: The Jesuits strive to integrate all aspects of their lives, including their spiritual, intellectual, and apostolic endeavors.
Magis: The Jesuits are challenged to strive for excellence in all that they do.
These principles are enshrined in the Constitutions of the Society of Jesus, which were written by Ignatius Loyola, the founder of the Jesuits. The Constitutions outline the structure and government of the Society, as well as the spiritual and apostolic principles that guide Jesuits.
The governing principles of the Society of Jesus are also reflected in the following practices:
Discernment: The Jesuits believe that it is important to discern God's will in all aspects of their lives. They use a variety of tools to help them discern, including prayer, reflection, and consultation with others.
Collaboration: The Jesuits believe that they can accomplish more by working together than they can by working alone. They collaborate with each other, as well as with laypeople and other religious orders.
Service: The Jesuits are committed to serving others, especially the poor and marginalized. They do this through a variety of ministries, including education, healthcare, and social justice work.
The governing principles of the Society of Jesus have guided Jesuits for over 500 years. They continue to be relevant today, as Jesuits work to build a more just and compassionate world.
Informed by Ignatian Spirituality and the central notion of “cura personalis,” we will endeavor to care for each person in our SJU family, our institutions, and our community through open dialogue, shared understanding and compassionate action.  
We seek to demonstrate a living faith that expresses itself in works for the greater divine service and the more universal good.  
The four Universal Apostolic Preferences of the Society of Jesus, 2019-2029 (with certain adaptations) from the Superior General’s letter:
To show the way to God; to renew His presence in the heart of human history
To walk with the poor, the outcasts of the world, those whose dignity has been violated, in a mission of reconciliation and justice;
To accompany young people in the creation of a hope-filled future;
To collaborate in the care of our Common Home; to collaborate with others in the construction of alternative models of life that are based on respect for creation.
	

https://jesuitseastois.org/discernment
What is Ignatian Discernment?
Ignatian discernment, sometimes called “discernment of spirits,” is the spiritual practice of noticing the movements within your heart and soul — your desires, thoughts, emotions — and identifying where they are coming from and where they are leading you.
Key Jesuit Terms
A.M.D.G. - Ad Majorem Dei Gloriam (Latin), meaning "For the greater glory of God." It is the motto of the Society of Jesus.
Contemplatives in action - A phrase that embodies the creative tension between Jesuits’ full embrace of concrete action and their attentiveness to where God may call them next. Lay organizations, such as the Jesuit Volunteer Corps, have also adopted this spiritual stance. In The Active Life, Parker Palmer writes, “Contemplation-and-action are integrated at the root, and their root is our ceaseless desire to be fully alive.”Cura personalis - (Latin), meaning care of the whole person. This fundamental value of the Society of Jesus involves three concepts, according to Brian McDermott, S.J.: Treating people as individuals and honoring their unique worth; caring for the “whole” person (including physical, emotional, intellectual, and spiritual health); and taking into account people’s backgrounds, including their family life, nationality, and culture.
Discernment - A process of discovering God’s direction and guidance in the concrete reality of our day-to-day lives. . . Discernment is a prayerful “pondering” or “mulling over” of the options facing you. Your goal is to understand them in your heart: to see them, as it were, as God might see them. In one sense, there is no limit to how long you might wish to continue this. Yet as you continue the process, some options should of their own account fall by the wayside while others should gain clarity and focus. It is a process that should move inexorably toward a decision. (Brother Charles J. Jackson, S.J.)
Ignatian - Refers to the defining characteristics and ethos of the Jesuits (or Society of Jesus), which was founded by Ignatius of Loyola.
Magis - (Latin), meaning more. The term traditionally used by St. Ignatius and the Jesuits to suggest the spirit of generous excellence--striving for the greater good--that drive our ministries.
Inculturation - A modern theological concept, which expresses that God is already present and active in a culture, and so our presentation of the Gospel to any given culture should be allowed to flourish in the “soil” of that culture.
Jesuit - A member of the Society of Jesus.
Our way of proceeding
“Certain attitudes, values, and patterns of behavior join together to become what has been called the Jesuit way of proceeding. The characteristics of our way of proceeding were born in the life of St. Ignatius and shared by his first companions.” Jerome Nadal writes that “the form of the Society is in the life of Ignatius [and they include] a deep personal love for Jesus Christ.” --Society of Jesus, General Congregation 34


What makes a successful center or institute?  (from Bard)
https://g.co/bard/share/19f7e87ac3fa
Clear vision and mission: The center or institute should have a clear vision and mission that is aligned with the goals of the university. This will help to ensure that the center or institute is using its resources effectively and making a meaningful contribution to the university's mission.
Strong leadership: The center or institute should have strong leadership from a director or executive director who has a vision for the center or institute and the skills to manage it effectively. The director should also be able to build relationships with faculty, staff, and students from across the university.
Adequate resources: The center or institute should have adequate resources to support its work. This includes funding for staff, equipment, and research.
Interdisciplinary collaboration: The center or institute should foster interdisciplinary collaboration among faculty, staff, and students. This will help to generate new ideas and solutions to complex problems. The center or institute should bring together faculty, students, and staff from different disciplines to work on common problems. This interdisciplinarity can lead to new and innovative approaches to research, teaching, and outreach.
Community engagement: The center or institute should be engaged with the community. This may involve providing services, conducting research that is relevant to the community's needs, or offering educational programs.
Has a track record of success. The center or institute should have a track record of success in achieving its mission and vision. This success can be measured in terms of research outputs, teaching outcomes, and outreach impact.
Successful centers and institutes at higher education institutions play an important role in advancing knowledge, training students, and serving the community. They are essential to the mission of universities to educate, discover, and create.


SJU strategic plan initiatives
Enrich Academic Quality and Distinction
Facilitate the expansion and development of professional schools and programs, while sustaining the prominence of the liberal arts and sciences at the core of the SJU academic experience.
Endorse and reaffirm a commitment to recruiting and retaining an outstanding and diverse faculty, including Jesuits.
Identify and construct quality programs for new student populations to complement our current strengths.
Develop and support new pedagogical spaces and cutting-edge facilities matching the quality of our academic product.
Expand Transformative Student Experiences
Develop and implement a strategic enrollment management plan that recruits and graduates talented and diverse students who embrace every aspect of an SJU education, enabling great success in their professional and personal lives.
Deliver an integrated and developmentally sequenced range of enriching experiential, leadership, spiritual and service opportunities to all students.
Empower students and alumni to lead successful, purpose-driven lives.
Create additional learning and gathering spaces that meet a variety of student and community needs.
Enhance and Promote Programs of National Prominence
Strengthen existing academic and co-curricular programs that are presently distinctive and allocate resources accordingly.
Leverage intercollegiate athletics to the maximum, positive benefit for the University.
Define two or three new initiatives that capitalize on institutional strengths, contribute favorably to our reputation and enhance the academic experience.
Promote these programs of distinction with a comprehensive marketing and communications strategy designed to strengthen our reputation.
Foster Greater Financial Strength
Implement a strategic financial model, through efficient utilization of resources, and promote a culture of innovation and accountability.
Significantly increase and expand donor support through a comprehensive campaign.
Diversify and expand revenue streams through the implementation of leading practices.
Provide competitive and comprehensive campus facilities.


SJU Administration
Typical departments in the administration of a university, other than academic programs, include:
https://g.co/bard/share/abbb2e223eac
Admissions and Enrollment: This department is responsible for recruiting, reviewing, and admitting new students, as well as managing student enrollment and records.
Financial Aid: This department provides financial assistance to students to help them pay for college, including scholarships, grants, loans, and work-study.
Registrar: This department maintains student records, including transcripts, grades, and course schedules.
Student Affairs / Student Life: This department provides support and resources to students outside of the classroom, such as housing, dining, student activities, and counseling services.
Campus Safety: This department is responsible for the safety and security of students and staff on campus.
Human Resources: This department manages the university's workforce, including hiring, training, and compensation.
Information Technology: This department provides and supports the university's technology infrastructure, including computers, software, and network services.
Facilities: This department is responsible for the maintenance and operation of the university's physical plant, including buildings, grounds, and equipment.
Finance and Budget: This department manages the university's financial resources, including budgeting, accounting, and investments.
Marketing and Communications: This department promotes the university to prospective students, donors, and the general public.
Research Administration: This department provides support to faculty and staff conducting research, including grant writing, contract management, and compliance with regulations.
Development and Alumni Affairs: This department cultivates relationships with alumni and donors to raise money for the university.
In addition to these general departments, many universities also have departments that provide specialized services, such as:
Disability Services: This department provides support and accommodations to students with disabilities.
International Programs: This department provides support to international students and faculty, as well as administering international exchange programs.
Continuing Education: This department offers non-credit courses and programs to the community.
Athletics: This department manages the university's athletic programs.
The specific departments that are found in a university's administration will vary depending on the size and type of institution. For example, a small liberal arts college may have a single department that oversees all student services, while a large research university may have separate departments for admissions, financial aid, housing, and dining.

Notes from scholarship on centers and institutes
3 missions of the university (C&Is are well suited to address the third mission)
education 
knowledge creation (i.e. research)
knowledge transfer, transmitting knowledge, innovation, public engagement; community partnerships
types of C&Is focusing on engaged research
Academic centers focused on community engaged research
Teaching/ Training-oriented academic centers focused on experiential learning
Practice-oriented centers engaged in community partnerships
Policy centers focused on community engaged research

Aims of community engaged centers (Akintobi et al. 2021)
support community engaged research
translate and disseminate research findings
develop partnerships
build capacity around community research

Solutions to common hurdles in community engaged research
Boundary spanners (people who connect the university and community) and asset-based approaches (considering and utilizing the assets of a community) can alleviate distrust due to power differentials
Supporting, advising, and preparing faculty on community engaged research can reduce burnout and lead to more sustainable projects; centers should also offer support to prepare students for this work
Reciprocal communication is key for building positive community relationships

Assessment and evaluation
Principles-Focused Evaluation may be a good fit for community engaged research centers, taking into account principles relevant to community/ university partnerships (trust, respect, communication)



"""
university_summaries = '''University sustainability plan summaries - 
Penn State University's "Sustainability Planning Guidebook" is a comprehensive resource designed to facilitate the integration of sustainability into various units within the university. It provides a structured six-step process and an array of tools that guide teams through formulating, implementing, and assessing sustainability plans.

**Summary of the Guidebook's Content:**

1. **Understanding Sustainability**: It starts with developing a shared understanding of sustainability, including its relevance to higher education and Penn State's goals aligned with the United Nations Sustainable Development Goals (SDGs).

2. **Assessing Current State**: Units are encouraged to evaluate their current sustainability engagement using the Sustainability Maturity Model. This model identifies different stages of sustainability integration, ranging from Starting to Transforming, and guides units in identifying their current stage and potential growth.

3. **Identifying Priorities**: A strategic look outside the unit identifies significant sustainability challenges and opportunities. This includes analyzing the impact of global sustainability challenges and developing strategies that leverage the unit's unique strengths and mission.

4. **Creating a Vision for Sustainability**: Units articulate a clear, inspirational vision of sustainability consistent with their identity and mission. The vision is linked with the university's strategic priorities to ensure it's aligned with broader institutional objectives.

5. **Setting Goals and Developing Metrics**: The guide advocates for setting strategic goals (Big Wins and Quick Wins) and developing specific, measurable, actionable, realistic, and time-bound (SMART) goals. It provides tools like strategy frameworks, brainstorming guidelines, decision matrices, and metric worksheets to aid this process.

6. **Developing an Implementation Plan**: Ultimately, units develop an implementation plan, which includes setting up essential support systems around the strategies, such as organizational structures, team learning, communications plans, and reporting/accountability mechanisms.

The guidebook encourages a collaborative and inclusive approach, involving students, faculty, staff, and external partners in the planning process. It also emphasizes the need for innovation and adaptability, acknowledging that sustainability plans will evolve over time.

Unique strategies and resources provided by the guidebook include:

- **Sustainability Maturity Model**: A tool to benchmark the current engagement with sustainability and identify the next steps for advancement.
- **Convergence Model**: A strategy for aligning sustainability with the unit's expertise, passion, resources, and sense of sustainability purpose.
- **Implementation Tools**: Specific worksheets, diagrams, and checklists designed to structure the planning and ensure key elements are not overlooked.
- **Collaborative Opportunities**: Advising on forming partnerships, engaging with community projects, and implementing student programs like EcoReps and Green Teams.

**Potential Benefits for SJU:**

Saint John’s University can benefit from adopting unique elements of Penn State’s approach that align with SJU's Jesuit values, such as the commitment to social justice, environmental stewardship, and economic feasibility. Some of these elements could enhance SJU's existing sustainability initiatives, while others could introduce new concepts or structures. Adapting the tailored planning process, support tools, and resources could also streamline SJU’s sustainability integration effort and promote a cross-campus culture of sustainability.

Moreover, Penn State's guidebook underscores the importance of aligning sustainability plans with global and institutional priorities, such as the SDGs and the university’s strategic plan, which could guide SJU in ensuring that its own sustainability efforts are strategically targeted and contribute to global and local sustainability solutions.

Harvard University has developed a comprehensive Sustainability Action Plan aimed at fostering systems and practices that protect the climate and environment, advance equity in society, and promote the wellbeing of people within the institution and beyond. The plan is grounded in Harvard's recognition of its responsibility and opportunity to innovate and scale sustainable solutions, drawing from decades of experience and its community's intellectual and financial resources.

Key elements of Harvard's Sustainability Action Plan include:

1. A Commitment to Fossil Fuel-Free Operations: Harvard aims to eliminate the use of fossil fuels on campus by 2050, targeting direct and indirect emissions. Before this, the university plans to achieve fossil fuel neutrality by 2026, compensating for greenhouse gas emissions and the health impacts from pollution resulting from the use of fossil fuels. Critical to this ambition are strategies for electrifying district energy systems, procuring fossil fuel-free electricity, converting stand-alone buildings to electric power, electrifying the university vehicle fleet, and prioritizing energy efficiency.

2. Sustainable Building Practices: Harvard is focused on enhancing sustainable design, construction, and operation of buildings and landscapes. This includes removing harmful chemicals from building materials, mitigating embodied carbon in construction materials, advancing equity and diversity in the value chain, and strengthening campus resilience to future climate impacts.

3. Low-Impact Living Systems: The plan underscores the need to overhaul crucial systems that impact daily life on campus. These systems include rethinking food systems to reduce emissions, accelerating toward a zero-waste future, reimagining transportation systems for reduced emissions and increased accessibility, enhancing water efficiency, and continuously improving energy efficiency in buildings.

4. Research and Leadership: Harvard's Salata Institute for Climate and Sustainability, founded with a $200 million donation, is key to driving research initiatives and practical solutions across various disciplines. The university also emphasizes the role of the Presidential Committee on Sustainability and the Harvard Living Lab in leading sustainability research and initiatives.

5. Student and Community Engagement: Harvard places a strong emphasis on involving students in sustainability through its Council of Student Sustainability Leaders and through the Harvard Innovation Labs, which supports climate entrepreneurship. Moreover, the plan highlights the importance of engaging with local, national, and international partners.

6. Transparent Governance and Accountability: Robust accountability structures, such as the Presidential Committee on Sustainability and regular reporting on targets and achievements, ensure that the plan remains a living document that evolves to strengthen Harvard's sustainability strategy.

For Saint John's University (SJU), adopting similar strategies could entail establishing clear targets for reducing carbon emissions, prioritizing sustainable building designs and operations, engaging students and faculty in sustainability research and projects, and fostering strong governance structures to ensure accountability and continuous improvement. Advancing sustainability in alignment with SJU's Jesuit values would involve incorporating social justice, environmental consciousness, and economic feasibility into the core of their sustainability programs, with an emphasis on community engagement and leadership in ethical environmental stewardship.

The Harvard plan can serve as an inspiring benchmark and a source of potential practices that SJU could adapt or adopt in the development or enhancement of their own sustainability initiatives.

Princeton University's Sustainability Action Plan aims to guide the institution toward a more sustainable future by 2026 and beyond. Following are key points from the plan that might serve as an effective inspiration for Saint John's University (SJU):

1. **Carbon Neutrality by 2046**: Princeton has set a goal to achieve carbon neutrality by its 300th anniversary in 2046, utilizing innovative and scalable solutions to reduce both direct and indirect greenhouse gas emissions.
   
2. **Water Conservation**: The Plan addresses a 26% reduction in water usage by 2046. It emphasizes the conservation of potable water, the use of reclaimed water, and a more mindful usage of water reflecting a connection to natural resources.

3. **Enhanced Stormwater Management**: An expansion of areas with enhanced stormwater management aligns with the goal to improve water quality and reduce runoff, contributing to the health of local waterways.

4. **Responsible Design and Development**: A commitment to integrative design for new buildings and renovations ensures that new construction meets sustainability targets, optimizes land use, and promotes efficient space utilization.

5. **Healthy Habitats**: Cultivating healthy and resilient ecosystems through restorative landscape management practices is another key element. The plan emphasizes habitat preservation, integration with land-use priorities, and engagement with natural surroundings.

6. **Sustainable Transportation**: Princeton's Plan nearly doubles the percentage of commuters using alternatives to single-occupancy vehicles by 2046. Initiatives like 'Revise Your Ride' encourage sustainable commuting habits.

7. **Zero Waste Goal and Sustainable Purchasing**: Aiming for zero waste, the Plan involves strategies for reduction, reuse, and recycling, integrating sustainability criteria in purchasing decisions to address the full lifecycle of products.

SJU can learn from these strategies by developing similar targets towards carbon neutrality, water conservation, stormwater management, sustainable construction, and landscape ecology. Additionally, they can promote a shift in transportation habits and embrace zero waste initiatives encompassing responsible consumption and procurement.

Notably, the Plan highlights the significant role of individuals within the campus community, acknowledging that fostering an ethos of sustainability through daily encounters can create lasting impact. This approach could resonate well with SJU’s focus on individual responsibility derived from its Jesuit values.

The inclusion of concrete projects, such as the solar field, LEDs retrofit, and stormwater management projects (e.g., rain gardens), provides tangible examples of how sustainability can be integrated into campus operations.

SJU could potentially adapt and implement several of these strategies within its own sustainability efforts, ensuring alignment with its values and commitment to environmental stewardship, social justice, and economic viability.

It's important to note that Princeton's Plan is comprehensive, collaborative, and deeply integrated with academic and operational functions, an approach that might greatly benefit SJU's sustainability endeavors.

The UC Berkeley Sustainability Plan for 2020 is an extensive and multi-faceted approach towards fostering a resilient, equitable, and carbon-neutral campus. The plan reinforces UC Berkeley's longstanding commitment towards environmental stewardship, public service, and academic excellence. It introduces a framework that intertwines various sustainability goals and strategies to decarbonize energy use, intelligently manage resources, and foster an inclusive community dedicated to solving global sustainability challenges.

**Unique and Effective Strategies, Practices, and Goals:**
1. Integration of Climate Resiliency and Environmental Justice: The plan incorporates climate resiliency and environmental justice into the sustainability framework, recognizing the unequal impacts of climate change on marginalized communities and emphasizing mitigation strategies.

2. Zero Carbon Campus by 2050: A significant ambition in the UC Berkeley Plan is the commitment to become zero carbon by 2050, which includes comprehensive strategies for reducing carbon emissions from all scopes including energy systems, transportation, and indirect sources.

3. Comprehensive Approach to Built and Natural Environment: The plan combines goals for building infrastructure with natural land stewardship, aiming to optimize sustainable development while enhancing campus ecosystems and biodiversity.

4. Systemwide and Campus-specific Goals: The document sets campus-specific sustainability goals that surpass the broader University of California systemwide goals, demonstrating local initiative and leadership.

5. Sustainable Services across Campus Operations: It outlines an integrative approach to managing campus operations, focusing on green operations, waste management, supply chain responsibility, and the novel Green Labs program aimed at reducing the environmental impacts of research.

6. Health and Wellness Intersectionality: The plan introduces strategies that connect sustainability to health and well-being, integrating food systems, mental health resources, and ergonomic practices, which are vital for building resilience.

7. Culture and Learning as Central Pillars: The UC Berkeley Sustainability Plan embeds sustainability into the campus culture and curricula. Emphasizing a diverse and inclusive culture, it supports the development of new sustainability and climate degrees and courses and enhances engagement outside of the classroom.

**Potential Benefits or Innovations for Saint John's University (SJU):**
- SJU could adopt a similarly comprehensive and highly integrative approach that aligns sustainability with its Jesuit values of social justice, environmental responsibility, and economic viability.
- SJU could consider setting ambitious scope 3 emissions targets, which include indirect emissions related to campus activities such as commuting and air travel.
- The creation of a Green Labs initiative could be highly innovative for SJU, focusing on reducing the environmental impact of scientific research—which is often resource-intensive.
- The intersectionality of health and sustainability introduced by UC Berkeley could serve to strengthen social justice and community well-being efforts at SJU.

**Conclusions for SJU:**
The UC Berkeley Sustainability Plan for 2020 offers a rich catalog of practices and goals from which SJU can draw inspiration. It serves as a model for integrating sustainability into every facet of a university's operations and academic mission. Particularly, the emphasis on resiliency, justice, and community engagement aligns well with SJU's Jesuit values. Integration and adoption of such sustainability strategies can position SJU as a leader in environmental responsibility within the higher education sector.

**Summary of Michigan State University's Stewardship and Sustainability Strategic Plan**

Michigan State University (MSU) has put forth an ambitious Stewardship and Sustainability Strategic Plan to advance its commitment to environmental stewardship and achieve climate neutrality by mid-century. This includes a target to reduce greenhouse gas emissions by 50% from their 2010 baseline, which translates to eliminating 292,934 metric tons of CO2. The plan recognizes the need to be a good steward of resources, ensuring long-term viability while maintaining quality and accessibility.

**Key Objectives and Strategies:**

1. **Financial Stewardship:** MSU plans to develop and implement a comprehensive financial model aligned with strategic priorities to ensure effectiveness and expand revenue sources. Key actions involve:
   - Transforming the university's budgeting process to support strategic priorities.
   - Launching a comprehensive Capital Campaign to increase private support.
   - Reviewing and updating strategic plans, including athletics, to align with national developments.
   - Pursuing external partnerships that align with MSU's mission and values.

2. **University Comprehensive Facilities and Land Use Plan:** The plan will include diverse perspectives, considering the history of the land MSU occupies, tribal consultations, and environmental impact reviews. It will:
   - Emphasize health and wellness in building designs, including WELL practices.
   - Integrate with frameworks for utilities, mobility, and open space management.
   - Include campus "district" plans for collaboration and innovation zones.

3. **Climate Neutrality and Sustainability Culture:** MSU aims for climate neutrality by 2050 and embedding sustainability into its culture. Actions include:
   - Developing a Sustainability and Climate Action Plan using a four-pillar framework focused on Campus, Curriculum, Community, and Culture.
   - Fostering resource stewardship through LEED principles, reducing emissions, and sourcing sustainable food.
   - Expanding sustainability education, research, and outreach opportunities.

4. **Sustainable Information Technology (IT) Strategic Plan:** This includes improving IT services for innovation in teaching and research, and providing operational excellence that supports informed decision-making and operating cost reductions. There is a push to expand access to advanced technologies like AI and virtual reality.

5. **Access to MSU Resources for Addressing Global Issues:** The plan focuses on ensuring the MSU community has tools and connectivity to succeed in various modalities. This involves:
   - Increasing access for persons with disabilities.
   - Expanding learning and applied learning opportunities through programs like micro-internships.
   - Partnering with businesses and communities to enhance reciprocal opportunities.

**Innovations and Benefits for SJU's Sustainability Plan:**
- Utilizing unit-level financial dashboards for strategic decision-making could provide SJU with a tool for resource allocation alignment.
- Implementation of WELL building practices and emphasis on green spaces reflect a commitment to health and wellbeing consistent with SJU's Jesuit values.
- MSU's focus on integrating sustainability into the curriculum, fostering research partnerships, and community engagement might serve as a model for SJU in creating a culture of sustainability.
- MSU's commitment to incorporating diverse perspectives, including the tribal histories of the land, and ensuring facilities are inclusive can enhance SJU's mission of social justice and inclusion.
- The comprehensive approach to climate neutrality with specific metrics and mid-century targets provides a long-term vision that SJU can emulate.

MSU's sustainability plan reflects its capacity as a large research institution to implement wide-ranging sustainability initiatives. SJU could consider which practices and strategies align with its own scale and mission, tailoring elements to fit its unique context as it continues to engage with environmental responsibility, social justice, and economic viability.

Brown University's Sustainability Strategic Plan, published in March 2021, is a comprehensive call to action, outlining the university's commitment to tackle the environmental challenges of the 21st century. It presents a blueprint for change, aligning with the university's longstanding mission to serve the community, nation, and world while integrating sustainability into its operations, education, and research.

Unique and Effective Strategies:

1. Scope-Based GHG Emissions Reduction: The plan categorizes greenhouse gas (GHG) emissions into scopes 1, 2, and 3 and sets specific reduction targets for each, with a commitment to net-zero emissions by 2040. This structured approach allows for targeted, measurable progress in reducing the university's carbon footprint.

2. Nutrient Pollution Reduction: Joining the Nitrogen Footprint Project, Brown seeks to decrease its nitrogen and phosphorus impact through focused changes in campus food purchases, aiming for a 25% reduction in red meat consumption by 2025 as part of this endeavor.

3. Human Health Emphasis: Brown plans to employ a holistic health strategy by eliminating potentially toxic chemicals from its operations, reducing noise and air pollution, and preparing its infrastructure for extreme weather induced by climate change.

4. Water System Impact: The plan examines the environmental benefits of stormwater reduction and grey water recycling and considers reallocating funding for water use and quality improvements based on these findings.

5. Biodiversity Preservation: Brown looks to influence biodiversity positively, not only by reducing negative impacts through responsible sourcing and reducing materials but also by incorporating the principles of the international Convention on Biodiversity into its operations and education.

6. Community Engagement in Sustainability: The strategic plan demonstrates Brown's intent to act as a regional leader in sustainability by engaging with local governments, organizations, and the public on renewable energy projects, legislation influence, and resilience initiatives.

Innovative Aspects for SJU:

- Adopting a multi-scope greenhouse gas management strategy could enhance SJU's existing environmental initiatives while providing clear benchmarks for progress.
- Incorporating health impacts related to environmental aspects—such as chemical exposures and air pollution—could offer a unique vantage point linking campus operations with community welfare.
- Brown's focus on nutrient pollution through food sourcing and reducing red meat consumption offers an interesting approach for SJU to consider, especially in light of Jesuit values that emphasize caring for our common home.
- The commitments to water impact reduction and biodiversity enhancement could provide SJU with actionable models on reducing resource use and ensuring sustainable procurement practices.
- Extending sustainability plans to include robust community engagement strategies can empower SJU to take a more proactive role beyond campus limits, touching on social justice and exercising its influence in the wider community.

The Brown University Sustainability Strategic Plan offers a compelling model for Saint John's University, with structured, measurable sustainability goals combined with a holistic approach to education, community engagement, and leadership that could offer new dimensions to SJU's sustainability planning.


# Summary of the University of Connecticut Sustainability Framework Plan

**Unique Strategies and Effective Practices:**
- Aiming for every new project to achieve net zero site energy.
- Benchmarking for energy performance using LEED Gold and EPA Energy Star Portfolio Manager score of 75 as minimum standards.
- Integration of renewable energy in new and existing buildings.
- Targeting a potable water use reduction of 40% and employing water reclamation, greywater systems, and rainwater harvesting.
- Sustainable Sites Initiative for land management and Low Impact Development (LID) strategies.
- Lifecycle assessment guiding purchasing decisions with emphasis on local procurement.
- Adaptation of transport systems to avoid increased parking demand and worse traffic congestion, considering alternative fuels and promoting bicycle-friendly initiatives.

**Key Goals:**
- Achieving carbon neutrality by 2050 focused on energy conservation, renewable integration, and minimizing Scope 3 emissions.
- Minimizing potable water consumption and optimizing rainwater management.
- Preservation and enhancement of ecosystems, promotion of sustainable farming and food production.
- Encouraging the use of environmentally preferable materials, reducing waste, supporting local and sustainable food sources.
- Incentivizing transition to sustainable transit and reduction in emissions associated with transportation.

**Potential Benefits to Saint John's University (SJU):**
- SJU could replicate UConn’s target for net zero site energy in new projects and retrofitting existing buildings.
- Adopting LEED Gold as a minimum benchmark for new constructions and renovations.
- Pursuing water conservation goals and innovative water management systems could be highly impactful given global water scarcity issues.
- Land management strategies, including revitalization of brownfields, and a strong focus on sustainable agriculture, can significantly enhance SJU's sustainability objectives.
- Leveraging SJU's purchasing power to influence markets towards more environmentally friendly products can be an effective strategy.
- Implementing a comprehensive transportation strategy could help reduce the carbon footprint associated with commuting while also improving campus life.

**Contrast to or Enhancement of SJU’s Initiatives:**
- UConn's rigorous benchmarking could set higher standards compared to SJU's current sustainability initiatives.
- The incorporation of the Sustainable Sites Initiative offers an enhanced approach to land use and ecosystem management that SJU could emulate.
- Energy use intensity (EUI) metrics for building performance may offer SJU a more nuanced evaluation tool for energy efficiency projects.
- The integration of community outreach within sustainability initiatives can bolster SJU’s commitment to environmental and social justice.

**Alignment with Jesuit Values:**
- The framework emphasizes responsible stewardship of the environment, commitment to community service, and education for sustainable development, which are in line with SJU's Jesuit values.

**Recommendations for SJU:**
- Explore renewable energy projects that are feasible within SJU's regional context.
- Evaluate the feasibility of adopting water management strategies used by UConn such as water reclamation and Low Impact Development strategies.
- Enhance sustainability in transportation by replicating UConn's model and creating incentives for alternative transportation modes.
- Develop purchasing policies that prioritize environmentally and socially responsible products and vendors.

# Conclusion
UConn's Sustainability Framework Plan provides innovative and comprehensive strategies that could serve as a reference model for SJU as it strengthens its commitment to sustainability, social responsibility, and economic viability. Adopting and adapting initiatives from this plan could further align SJU with its Jesuit mission and improve its overall sustainability performance.

The University of Vermont's Comprehensive Sustainability Plan (CSP) for 2023-2040 presents a strategic approach to amplifying and expanding upon its already significant sustainability efforts. The plan underscores the university's commitment to achieving carbon neutrality by 2030 and integrates sustainability into its operations, governance, planning, research, and learning practices.

Unique and effective strategies, practices, and goals outlined in the CSP include:

1. Decarbonization: UVM sets forth ambitious goals of 60% GHG emissions reduction from 2007 levels by 2024 and reaching carbon neutrality by 2030. This includes optimizing renewable energy technologies such as solar and piloting geothermal projects, as well as purchasing locally-sourced carbon offsets.

2. Energy and Climate: The university plans to develop a campus energy plan and pursue renewable energy heating systems for buildings, increase the payback period for the Green Revolving Loan Fund, and enhance utility metering for better energy use tracking.

3. Transportation: UVM aims to decrease its fleet size, transform its light-duty vehicles to 100% electric by 2040, promote sustainable commuting methods, and implement at least 20% EV charging spaces in new parking lots.

4. Operations: Prioritizing circularity, UVM commits to increasing spending on Vermont-grown food to 25% by 2030 and intends to strengthen waste reduction and recycling efforts campus-wide.

5. Landscape: The plan includes prioritizing electric grounds equipment and enhancing sustainable and native plantings to develop an eco-friendlier campus landscape.

6. Governance and People: UVM plans to create a Leadership Committee to track the CSP implementation, focus on socially responsible investing, develop workforce training programs for Vermont's green economy and improve sustainable purchasing practices.

7. Research and Learning: The university is launching a Sustainable Solutions Lab to engage the campus as a 'living lab', promoting applied student research. There’s also a commitment to integrating sustainability into the core curriculum and across various academic programs.

8. Diversity, Equity, and Inclusion (DEI): UVM integrates DEI into its sustainability strategies, aiming to create a diverse and globally aware university community.

For Saint John's University (SJU), several elements of UVM's CSP could serve as enhancements to its existing sustainability initiatives:

- The creation of a Leadership Committee may heighten the accountability and transparency of SJU's sustainability efforts.
- SJU could model UVM’s impactful “living lab” approach to connect sustainability challenges with academic inquiry.
- UVM’s dedication to local food systems and procurement practices could align with SJU's Jesuit values of community engagement and support for local economies.
- The emphasis on campus-wide participation, from workforce development to broad educational opportunities, may strengthen SJU's community involvement in sustainability.

Enhancing SJU's sustainability initiatives could involve adopting a similarly broad, multi-faceted approach to sustainability, incorporating a blend of local action, academic integration, community involvement, and clear goals like those set by UVM.

# Summary of Northern Illinois University's Draft Sustainability and Climate Action Plan

**Executive Summary:**
- The plan addresses urgent climate change and biodiversity loss and its disproportionate impact on vulnerable communities.
- NIU's definition of sustainability focuses on thriving, diverse, equitable communities now and in the future.
- The plan outlines actions in three categories: Climate Mitigation and Adaptation, Operations, and Academics, Administration, and Community Engagement, with a goal to achieve net-zero greenhouse emissions by 2050.
- Emphasis is placed on equity, diversity, inclusion, and the creation of a culture of sustainability through education, outreach, engagement, and extensive infrastructure upgrades. 

**Unique Strategies and Practices:**
1. Building Decarbonization:
   - Developing a master plan for building automation systems.
   - A comprehensive facilities plan that includes infrastructure upgrades for a 50% emissions reduction by 2030.

2. Renewable Energy:
   - Formulating a strategic plan for renewable energy with the ambition of carbon neutrality in energy consumption by 2040.

3. Transportation:
   - In-depth analysis of the transportation carbon footprint.
   - Launch visible measures to reduce carbon emissions within three years, including fleet vehicle replacement and promoting sustainable commuting.

4. Food and Dining:
   - Identifying sustainable options for food purchasing and promoting low-carbon footprint meal options.

5. Grounds:
   - Implementing landscape management policies that harmonize environmental, economic, and social needs.
   - Restoring native habitats and biodiversity.

6. Education and Outreach:
   - Enhancing the curriculum to include sustainability across disciplines.
   - Fostering immersive experiences and promoting sustainability research.

7. Water:
   - Assessing and reducing water consumption and managing stormwater on campus.

8. Waste:
   - Conducting comprehensive waste audits and achieving “zero waste” through diversion strategies.

9. Purchasing:
   - Developing sustainable procurement policies across multiple commodity categories.

**Innovative Elements for Saint John's University's Consideration:**
- The integration of a university-wide climate vulnerability and risk assessment to prioritize climate adaptation and resilience strategies.
- Aligning with global initiatives, such as the United Nations Framework Convention on Climate Change's (UNFCCC) Race to Resilience challenge, and the Second Nature Climate Resilience commitment.
- The commitment to developing a living laboratory approach for the campus that promotes student and community engagement with sustainable practices.
- Creation of a sustainability dashboard to enhance transparency and track the university's sustainability performance.
- Forming a Presidential Commission on Sustainability to provide leadership and collaborative governance on sustainability issues.

**Alignments with SJU's Values:**
- The plan emphasizes Jesuit values of social justice, equity, and stewardship of the environment, aligning with Saint John's University's mission.
- It underscores the significance of collective responsibility and action — a central tenet of SJU's commitment to community service and engagement.

**Enhancements to Existing Initiatives:**
- Expansion of the current scope of engagement and educational experiences to include sustainability themes in all aspects of university life and learnings.
- The comprehensive strategy for waste management and water conservation could elevate SJU's green initiatives.
- Potential to enhance SJU's current digital communication strategies with the implementation of a sustainability-centered website and data dashboards. 

**Conclusion:**
NIU's Sustainability and Climate Action Plan charts a detailed and ambitious path forward, laying out measures for carbon neutrality and an inclusive sustainability culture integrated with the university's operations and academic mission. The plan's innovative and participatory elements offer valuable insights that Saint John's University can consider while developing or enhancing its sustainability initiatives.

Summary of the 2021 OHIO Sustainability and Climate Action Plan:

The Ohio University (OU) Sustainability and Climate Action Plan is a strategic document outlining the institution's approach to achieving carbon neutrality within the framework of academic requirements as stipulated by the Presidents' Carbon Commitment. The plan outlines ambitious goals intended to enhance OU's national reputation as a laboratory for sustainability.

Key Attributes of the Plan:
1. Alignment with AASHE STARS and UN SDGs – The plan aligns with recognized frameworks, enabling streamlined reporting and promoting national recognition.
2. Categories in the Plan – The plan incorporates sixteen thematic areas divided into three Sustainability Hubs (Administration, Living, and Infrastructure). Each category details current status, goals, targets, strategies, and cost/benefit analyses.
3. Community Engagement – Feedback from the university and local community was integrated into the plan, ensuring comprehensive and diverse perspectives.
4. Triple Bottom Line Approach – The strategy implementation aims to positively impact people, planet, and prosperity, aligning with the ethical commitments and values of SJU.

Strategies and Goals:
The plan suggests unique and innovative strategies that could serve as an inspiration for SJU's sustainability planning. These include:
- Administrative Support for resilience and sustainability with innovative funding mechanisms outside of general funds.
- Robust infrastructure focusing on reducing building impacts through sustainable construction, renovation, and demolition.
- Emphasis on diversity, inclusion, and employee wellbeing in Human Resources.
- Commitment to local food economies and encouraging mindful food choices.
- Creating experiential learning opportunities through the maintenance of healthy, biodiverse landscapes.
- Fostering sustainability, diversity, and inclusion as key student attributes in recruitment and retention efforts.
- Reducing carbon emissions from transportation by promoting efficient and healthy alternatives to single-occupancy vehicles.
- Pushing for research incentivization in sustainability and carbon neutrality.

Implementation and Tracking:
- Detailed implementation guides will be created, outlining metrics, responsible parties, and progress tracking methods for each category.
- A Sustainability Project Laboratory (SPL) will facilitate flexible and evolving strategy implementation by various campus stakeholders.
- Regular reporting mechanisms will ensure accountability and transparency in tracking the university's progress toward sustainability goals.

Relevance to Saint John's University (SJU):
Such a comprehensive plan could influence SJU in several ways:
- A robust focus on diversity and inclusion in sustainability planning can enrich SJU's Jesuit principles of social justice.
- Engaging the SJU community, including students and local stakeholders, can strengthen the university's mission and align with its values.
- The SPL model as a living lab could be an effective approach for SJU to foster experiential learning and actionable research among students.
- Leveraging frameworks such as AASHE STARS could enhance external recognition for SJU's sustainability efforts.

In conclusion, the 2021 OHIO Sustainability and Climate Action Plan provides a robust framework and clear direction for achieving sustainability goals, which SJU could adapt in alignment with its own values, to enhance environmental responsibility, social justice, and economic viability.

**Summary and Analysis of the University of Kentucky Sustainability Strategic Plan for Saint John's University**

**Overview:**
The University of Kentucky (UK) has created a comprehensive Sustainability Strategic Plan, with the principal goal of integrating sustainable practices across academic, research, health care, and operational domains over a five-year period. The plan encompasses six main sectors: Materials Management, Energy, Food and Dining Services, Transportation, Buildings and Grounds, and Greenhouse Gas Emissions. Water Conservation was added as the seventh focal area. Detailed strategies and tactics have been developed, along with target dates, responsible parties, and performance metrics.

**Unique and Effective Strategies:**

1. **Materials Management:** UK aims to increase waste diversion to 50%, implement a sustainable purchasing protocol, conduct waste audits, and enhance education related to waste management. This area stresses the importance of understanding the entire life cycle of consumed materials.

2. **Energy:** The university seeks to reduce energy consumption through a multi-faceted approach, which includes upgrading buildings for better energy efficiency, optimizing lighting, increasing energy awareness, and improving utility plants and distribution systems.

3. **Food and Dining Services:** UK attempts to increase the sustainability of the campus food system by integrating sustainability metrics into dining operations, improving sourcing, and expanding food insecurity programs.

4. **Transportation:** The plan promotes a shift towards multi-modal, healthy, and environmentally friendly transportation methods by improving public transit access, expanding bicycle infrastructure, and incentivizing other transportation alternatives to single-occupancy vehicles.

5. **Buildings and Grounds:** A key distinctive feature is the use of the campus as a "living laboratory/classroom," designing and maintaining buildings and grounds to support the university's sustainability commitment.

6. **Greenhouse Gas Emissions:** UK has committed to a 25% reduction in emissions by 2025, with detailed sub-strategies for energy conservation, waste reduction, and transportation changes.

7. **Water:** The university outlines a strategic plan to maximize stormwater management, protect water quality, and conserve resources, relying on existing strengths like the Water Quality Management Program.

**Potential Beneficial and Innovative Elements for SJU:**

1. **Water Strategy Integration:** The comprehensive emphasis on water conservation could be especially beneficial for SJU, as conservation and stormwater management are essential in many regions.

2. **Campus as Living Laboratory:** UK's approach of integrating sustainability into research and teaching by using campus infrastructure as a practical learning environment could serve as a distinctive feature for SJU's sustainability plan.

3. **Community Engagement:** UK's strong focus on community involvement could inspire SJU to create similar avenues for student and staff engagement in sustainability initiatives and allow for a collaborative campus climate on sustainability practices.

4. **Student Initiatives:** Encouraging student-led sustainability projects and organizations could be a scalable practice for SJU, as it fosters a culture of environmental responsibility and innovation from the ground up.

5. **Multi-Modal Transportation:** The targeted efforts to enhance transportation options align with SJU's Jesuit values of community and social justice by promoting accessibility and health benefits while reducing carbon emissions.

6. **Sustainability Challenge Grant Program:** SJU could benefit from implementing a similar funding structure to stimulate interdisciplinary research and projects for sustainability, based on UK's model.

**Enhancements and Contrasts with SJU's Existing Initiatives:**

- SJU's sustainability initiatives could be enhanced by adopting similar comprehensive waste diversion tactics, robust energy optimization programs, and community-focused transportation planning.
- A contrast may be seen in the level of student engagement UK has achieved in sustainability, which could provide a benchmark for SJU to aspire towards.
- UK's tactic of developing operational protocols for building maintenance and urban forest management could augment SJU’s existing practices by providing clear guidelines and action plans.

**Conclusion:**
The University of Kentucky Sustainability Strategic Plan offers a well-structured and multi-dimensional approach to campus sustainability. The explicit strategies for energy, materials, food, and transportation, combined with commitments to emissions reductions and water conservation, provide a robust framework that can inform the development of SJU’s sustainability plan. Especially pertinent are the innovative practices linked to curriculum integration, stakeholder engagement, and student involvement that resonate with SJU’s values and could significantly progress its environmental responsibilities, social justice considerations, and economic viability in sustainability efforts.

The University of California's Sustainable Practices Policy establishes objectives in 13 areas: green building, clean energy, climate action, transportation, sustainable operations, zero waste, procurement, foodservice, water, healthcare, performance assessment, health and well-being, and inclusive justice. This comprehensive policy aims to minimize the environmental impact of university operations and serve as a living lab for sustainable practices. 

The policy includes ambitious targets like achieving at least a 90% reduction in total greenhouse gas emissions across all scopes by 2045, obtaining 100% clean electricity by 2025, and not using on-site fossil fuel combustion for new buildings from 2024 onwards unless essential. It also covers zero waste goals, such as reducing per capita solid waste generation by 50% by 2030 and achieving 90% waste diversion from landfill. 

In procurement, there's a strong commitment to sourcing sustainable products, including a stipulated percentage of spend on green and socially responsible products. There are guidelines for promoting sustainable foodservice operations, achieving reductions in potable water consumption, and providing education to embed sustainability across all university activities. The policy also supports healthy food options, alternative transportation, resources conservation, and inclusive procurement practices.

An anti-racism, diversity, equity, and inclusion (DEIJ) assessment will be part of future policy revisions, ensuring these principles are integrated throughout the policy. Compliance and reporting will be overseen by the Executive Vice President - Chief Financial Officer, and performance is evaluated in an annual report to the Regents, with revisions to the policy planned every three years. 

For Saint John's University (SJU), considering its Jesuit values and commitment to environmental responsibility, social justice, and economic viability, these policy components could serve as both a framework for SJU's sustainability planning and a benchmark against which to measure its progress. The emphasis on campus-wide involvement, continuous improvement, and the integration of sustainability into broader institutional goals align well with SJU's values and can guide its own sustainability journey.

Summary of UCLA's Sustainability Plan 2022:

UCLA has developed a comprehensive Sustainability Plan, focusing on creating a thriving, healthy, diverse, and resilient community. The plan integrates environmental health, social equity, and economic vitality while recognizing the traditional land caretakers of the Los Angeles basin.

The Sustainability Plan aims to:
1. Foster an environmentally conscious, socially just, and fiscally responsible culture.
2. Engage the campus community across academics, operations, and community relations.
3. Build upon existing strengths and establish new goals in sustainability.
4. Encourage immediate action and long-term investment for a sustainable future for UCLA.

The plan has five thematic areas:
- Planetary + Human Health
- Equity, Diversity, Inclusion, + Justice
- Curricula + Research
- Sustainable Campus
- Engagement

The plan aligns with the UC Policy on Sustainable Practices, addresses 12 regional Los Angeles County sustainability goals, and contributes to global sustainability initiatives, including the United Nations Sustainable Development Goals (UN SDGs).

Key goals of the UCLA Sustainability Plan include:
- Increasing awareness of the interconnectivity between planetary and human health.
- Prioritizing social equity to ensure sustainability for all.
- Expanding sustainability-focused curricula and research.
- Achieving climate neutrality and advancing renewable energy objectives.
- Reducing waste generation and promoting sustainable consumption and production.
- Reducing potable water consumption amid persistent drought conditions.
- Increasing campus sustainability literacy and culture through engagement.
- Supporting biodiversity and integrating the campus landscape into regional ecological systems.
- Certifying green buildings on campus to improve environmental and human health.
- Reducing single occupancy vehicle commuting rates.

To execute this plan, UCLA engages students, faculty, and staff in collaborative efforts, and utilizes interdisciplinary approaches, such as the Sustainable LA Grand Challenge and Sustainability Action Research. The plan is structured with measurable targets and actions, and is implemented by key players across various departments and offices within UCLA.

The Sustainability Plan is a dynamic document that will evolve over time, reflecting UCLA's commitment to sustainability leadership, both locally and globally.

**Summary of USC Sustainability 2020 Plan:**

**Introduction and Commitment:**
The USC Sustainability 2020 plan outlines the university's vision to address global environmental challenges through innovative practices in teaching, research, operations, and facilities. Recognizing the need to adapt to a changing planet and address issues like climate change, resource reduction, and biodiversity loss, USC is committed to sustainable development as defined by the Brundtland Commission. The university emphasizes a holistic approach, considering the ecological, economic, and equity dimensions, particularly in the face of California's drought and rising costs of energy and waste disposal.

**Key Sustainability Goals:**
The plan is organized around seven core areas:

1. **Education and Research:**
   - Fostering environmental literacy among students and faculty.
   - Developing degree programs focused on sustainability.
   - Enhancing research that is cross-disciplinary and transformative.

2. **Community Engagement:**
   - Raising awareness of sustainability practices on campus.
   - Converting the campus into a living laboratory for sustainability.
   - Engaging local communities and creating an alumni network focused on sustainability.

3. **Energy and Greenhouse Gas Mitigation:**
   - Reducing greenhouse gas emissions by 20% per square foot from the 2014 baseline by 2020.
   - Leveraging energy risks and opportunities, including advancing renewable energy and energy efficiency.

4. **Sustainable Transportation:**
   - Decreasing single-occupancy vehicle commutes.
   - Boosting participation in alternative transportation programs.

5. **Sustainable Procurement:**
   - Engaging 75% of departments in responsible purchasing by 2020.
   - Incrementally increasing the percentage of food purchased from sustainable sources.

6. **Waste Diversion:**
   - Achieving a waste diversion rate of 75% by 2020.
   - Enhancing recycling and waste reduction education.

7. **Water Conservation:**
   - Reducing potable water use significantly by 2020.
   - Increasing conservation awareness and developing behavior-modification campaigns.

**Innovative Strategies and Practices:**
Key innovative strategies include using the campus as a living lab for sustainability projects, creating a sustainability-focused curriculum, engaging the community through an Urban Sustainability Extension or Clinic, and establishing a Green Revolving Fund. Prominent actions include a plan to plant thousands of trees, developing an interdisciplinary sustainability curriculum committee, the adoption of a USC bike plan, and a campus-wide composting initiative.

**Potential Benefits for Saint John's University:**
Saint John's University (SJU) can learn from strategies like the Green Engagement Fund that encourages student participation in sustainability projects, expanding metering and targeting water conservation, and the development of comprehensive waste and recycling programs. SJU can also benefit from the collaborative approach taken by USC, involving various stakeholders, including students, staff, faculty, and the local community, to foster a comprehensive sustainability culture. Emphasizing the Jesuit values of social justice and stewardship, these initiatives, particularly those that engage the surrounding community and promote interdisciplinary research, could align well with SJU's mission.

Overall, USC's plan is a robust framework advocating for strategic, community-engaged sustainability actions that integrate research, education, and operations towards environmental stewardship. Saint John's University can draw inspiration from this evidence-based, collaborative approach as it crafts and refines its own sustainability initiatives.

The University of California, Davis (UC Davis) has developed a comprehensive sustainability plan entitled "Blueprint for a Green Future." The blueprint was prepared by Vice Chancellor Stan Nosek's Sustainability Advisory Committee, chaired by Jill Blackwelder. The plan defines sustainability, outlines guiding principles and values, and categorizes sustainability efforts into five main areas: Campus Planning and Transportation, Education and Outreach, Energy and Atmosphere, Green Buildings, and Materiel Management. 

The blueprint emphasizes a holistic, integrated, and continuously improving approach to sustainability that links academic pursuits with campus development. The plan highlights the need for a shared responsibility for sustainability among all campus community members. The document also seeks to be a "living" plan, open to revision and responsive to new insights.

To initiate the sustainability effort, the committee assembled its top 15 high-priority recommendations requiring an estimated $980,000 for implementation, with ongoing annual operation and maintenance costs. The recommendations are intended to establish attainable goals and to promote discussion and long-term planning for sustainability at UC Davis. 

The plan presents a detailed discussion for each of the five areas, providing a brief description of the area, UC Davis's current approach, options matrix, efforts to date, recommendations for action, challenging long-term goals, and sources for innovative ideas.

Key recommendations include:

1. Implementing sustainable transportation by improving pedestrian and bicycle pathways, advocating for alternative transportation, and reducing the reliance on carbon-fueled vehicles.
2. Advancing sustainable water management by enhancing water quality, reducing stormwater discharge, and studying reclaimed water use.
3. Fostering community engagement in sustainability efforts, creating a green map to raise awareness, and offering teaching opportunities through campus biodiversity.
4. Increasing the use of renewable energy, enhancing building energy management systems, and ensuring energy conservation measures align with UC Clean Energy and Green Building policy goals.
5. Promoting green construction methods and materials while retrofitting existing buildings to higher environmental standards.
6. Expanding sustainable practices in purchasing, food services, and waste management. Encouraging recycling programs and sustainable chemical usage, and waste disposal methods.

The blueprint recognizes UC Davis's unique assets and challenges due to its large size, diverse infrastructure systems, and status as a top research institution in the United States. The plan's holistic approach, focus on integration, and commitment to sustainability encompass the full spectrum of campus life and operations while promoting education, research, and community participation.

The blueprint aims to be a model for other institutions, offering a strategic direction that advances sustainability within a university setting while maintaining a mindful balance of ecological, economic, and social considerations. It is forward-thinking and acknowledges the importance of sustainability in higher education and its broad impacts on society and future generations. UC Davis's blueprint could serve Saint John's University as a point of comparison and inspiration as it develops its sustainability plan, aligning with its Jesuit values of environmental responsibility, social justice, and economic viability.

The University of Virginia (UVA) has developed a comprehensive Sustainability Plan for 2020-2030 that builds on their previous sustainability efforts and sets ambitious goals for the coming decade. Below is a structured analysis of the key aspects of the plan which Saint John's University (SJU) could consider for comparison or inspiration for its own sustainability initiatives, in alignment with its Jesuit values and focus on environmental responsibility, social justice, and economic viability.

**Governance and Collaboration:**
UVA aims to incorporate sustainability leadership at all decision-making levels by integrating environmental, economic, and equity considerations. This approach promotes accountability and ensures that sustainability goals are part of the university's core operations and planning.

*Unique Strategy:* UVA plans to develop school and unit-level action plans aligned with university-wide sustainability goals, and evaluate financial investments to support transformational change in sustainability.

**Engagement with Community and Service:**
UVA's plan emphasizes partnership with local and regional communities to foster sustainable, equitable, and healthy living spaces, acknowledging the disproportionate impacts of climate change on underserved populations.

*Innovative Practices:*
- Strengthening formal connections for collaborative initiatives between UVA and community stakeholders.
- Partnering on policies and programs aimed at K-12 education, food justice, transportation, resilience, and health.

**Stewardship of Resources:**
The plan includes measurable "30 by 30" goals to be achieved by 2030, such as reducing water use, reactive nitrogen emissions, and waste footprint by 30% and increasing sustainable food purchases to 30% of the annual total. UVA also aims to be carbon neutral by 2030 and fossil fuel-free by 2050.

*Effective Strategies:*
- Developing Climate Action Plans for 2030, 2040, and 2050.
- Addressing UVA’s energy sources, infrastructure, buildings, fleet, and transportation to reach these carbon neutrality and fossil fuel goals.

**Curriculum and Research (Discover):**
The plan calls for an enhancement of sustainability-focused teaching and curriculum development, as well as promoting UVA's sustainability research and fostering collaborations for community-engaged learning.

*Potential Benefits:*
- Evaluation of Sustainability Faculty Teaching Fellows to provide interdisciplinary learning experiences.
- The possibility of creating a Summer Sustainability Program and an Undergraduate Community Green Scholars Program to offer experiential learning and professional development.
- Continuation and evaluation of the Environmental Resilience Institute to position UVA as a leader in linking science, policy, and practice for environmental challenges.

SJU could be particularly interested in UVA’s commitment to transdisciplinary approaches, which can foster collaboration among different academic fields, and UVA’s initiative to ensure real-world sustainability experience for students. The "30 by 30" targets provide clear, achievable goals that can be mirrored or adapted by SJU in its efforts.

**Summary for SJU:**
UVA's Sustainability Plan is characterized by ambitious goals, a commitment to community partnership for equitable sustainability, and an integrated approach across teaching, research, and operations. The plan encompasses a long-term vision with concrete short-term targets, which aligns with SJU's principles of long-term thinking and action within its Jesuit framework. Unique strategies like school and unit-level action plans and the commitment to a carbon-neutral and fossil fuel-free future are examples SJU could potentially emulate or draw inspiration from in strengthening its sustainability agenda.

Stetson University's Environmental Stewardship Plan, developed in Fall 2011 and revised multiple times up to November 2015, presents a comprehensive strategy to achieve carbon neutrality by 2050, emphasizing sustainability across various aspects of campus operation. Unique elements of Stetson University's plan and potential benefits for Saint John's University (SJU) to consider might include:

1. Structured Carbon Audits: Stetson performs regular Carbon Audits, which measure the effectiveness of their sustainability initiatives and inform decision-making. Conducted by students using Clean Air Cool Planet's Carbon Calculator, this engagement in practical learning aligns well with SJU's Jesuit values of education and stewardship.

2. Commitment to Interim and Long-Term Goals: Reduction goals are set for specific years leading up to 2050, ensuring accountable progress is made continuously. Their strategy offers insights into proactive planning and goal-setting, which SJU may integrate into its plan.

3. Scope Emissions Categorization: Emissions are divided into Scope One (direct), Scope Two (indirect from energy consumption), and Scope Three (other indirect emissions such as travel). By understanding these categories, SJU can target specific areas for more effective carbon footprint management.

4. Emphasis on Awareness and Behavioral Change: By focusing on developing awareness and changing behaviors within the campus community with the help of partners like Cenergistics, Stetson strives to instill sustainable practices that extend beyond the campus. This could reinforce SJU's mission to influence broader society for social justice and environmental responsibility.

5. Integration into Curriculum: Stetson embeds environmental challenges and climate change education into the core curriculum, ensuring all students graduate with sustainability knowledge. SJU could mirror this approach, tying it to its values of lifelong learning and ethical leadership.

6. Investment in Green Technologies: Stetson commits to using LED lighting, solar power, and other clean technologies, which SJU could capitalize on, particularly when considering innovations available since Stetson's latest plan revision.

7. Facilities' Development and Maintenance: Stetson aims for LEED certification for new and renovated buildings, promoting a sustainable built environment, an area where SJU could also focus, ensuring that infrastructure advances meet environmental standards.

8. Advocacy for Public Policy: Recognizing the crucial role of policy, Stetson plans to influence decisions toward carbon neutrality collaboratively with other institutions. SJU might also seek to take a more active role in advocacy, true to its values of social engagement.

9. Water Conservation Measures: Stetson's aggressive water conservation strategies have resulted in significant water savings, even as enrollment increased. SJU could adopt similar measures, particularly those yielding high social returns on investment and incorporating reclaimed water use and stormwater management.

10. Proposed Green Initiatives: Stetson lists several specific projects under consideration to reduce Scope One, Two, and Three emissions, many of which reflect innovative approaches that could inspire similar initiatives for SJU.

Key Takeaways for SJU:

- Incorporating a culture of sustainability by engaging students in green audits and integrating environmental education into the curriculum.
- Setting measurable interim goals to ensure accountability and steady progress toward carbon neutrality.
- Advocating for public policy changes that support sustainability.
- Exploring water conservation tactics and other initiatives that could be adopted or serve as inspiration for SJU's sustainability programs.

SJU can benchmark against Stetson's detailed approach as it develops its sustainability plan, taking into account the evolving landscape of technology and policy to enhance its commitment to environmental responsibility and social justice.


'''

# Combine the contents for input
combined_input = msu_plan_contents + "\n\n" + jesuit_principles_contents + "\n\n" + foundational_document_contents + "\n\n" + university_summaries

# Define the prompt for generating the sustainability plan
prompt = """
    Develop a detailed and comprehensive sustainability plan for Saint John's University (SJU) that emulates the structure of Michigan State University's strategic plan. This plan should integrate insights from the following key documents: SJU's Jesuit and Foundational documents, the summary of 17 university sustainability plans, and Michigan State University's Sustainability Plan. Ensure the plan includes:

    - Adopting MSU’s Plan Structure: Follow the format and structure of Michigan State University’s plan, especially their “Stewardship and Sustainability” practices. Include sections like Title, Introduction, Goals, Objectives with Strategies/Actions, and Illustrative Indicators/Metrics.

    - Integrating Jesuit Principles: Deeply infuse SJU’s Jesuit values into every part of the sustainability plan. Highlight how these values influence the setting of goals, objectives, and strategies, ensuring a seamless integration with the university's ethos.

    - Leveraging Insights from 17 University Plans: Incorporate innovative and effective strategies from 17 other university plans, ensuring SJU’s plan is unique and tailored to its specific challenges and opportunities.

    - Climate Neutrality and Measurable Outcomes: Outline a clear, measurable pathway towards climate neutrality, including specific goals, objectives, strategies, actions, and indicators/metrics.

    - Actionable and Community-Focused Plan: Create a plan that is both practical and achievable, with a strong emphasis on community engagement, educational initiatives, and technological innovations.

    - Comparative Analysis and Innovation: Integrate effective and innovative elements from the 17 university plans, aligning them with SJU’s Jesuit values and context.

    - Benchmarks and Ambitious Goals: Use insights from the 17 plans as benchmarks to set ambitious, context-appropriate sustainability goals for SJU.

    - Broad Coverage and Depth: Ensure the plan covers a broad range of sustainability topics, showing a deep understanding of the challenges and opportunities in sustainability for SJU.

    The final document should vividly reflect SJU’s commitment to environmental responsibility, social justice, and economic viability, and be formatted for compatibility with a Word document. It should draw extensively on the insights from the provided documents, showcasing SJU’s unique approach to sustainability grounded in its Jesuit values and traditions.

    Don't mention MSU in the final document, just emulate the structure. Elaborate on each object to a greater extent than MSU did; likely double the length.
"""

# Generate the sustainability plan
print("Generating the Sustainability Plan for SJU...")
model_result = get_input(prompt, combined_input)

# Define the filename for the output
output_filename = 'sju_sustainability_plan_draft.txt'

# Save the generated plan to a file
with open(output_filename, 'w') as file:
    file.write("-" * 50 + "\n")
    file.write(model_result)
    file.write("\n" + "-" * 50)

print(f"Sustainability plan has been saved to {output_filename}")
