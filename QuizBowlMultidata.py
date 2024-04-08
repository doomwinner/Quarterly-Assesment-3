import sqlite3
import json

# Create a connection to the SQLite database
conn = sqlite3.connect('quiz_questions.db')
c = conn.cursor()

# Create a table to store quiz questions
c.execute('''CREATE TABLE IF NOT EXISTS questions (
                id INTEGER PRIMARY KEY,
                category TEXT,
                question TEXT,
                options TEXT,
                correct_answer TEXT
            )''')

strategic_management_questions = [
    ("Strategic Management", "What is SWOT analysis?", 
     '["A. Strengths, Weaknesses, Opportunities, Threats", "B. Sales, Work, Objectives, Targets", "C. Systems, Workforce, Operations, Technology", "D. Strategy, Work, Objectives, Team"]', 
     "A"),
    ("Strategic Management", "What is Porter\'s Five Forces?", 
     '["A. A marketing framework", "B. A pricing strategy", "C. A strategic planning tool", "D. A project management approach"]', 
     "C"),
    ("Strategic Management", "What is the purpose of Porter\'s Generic Strategies?", 
     '["A. To identify potential target markets", "B. To gain a competitive advantage in a specific market segment", "C. To maximize shareholder value", "D. To minimize operational costs"]', 
     "B"),
    ("Strategic Management", "What is meant by the term \'Core Competency\' in strategic management?", 
     '["A. Basic skills required for all employees", "B. Specialized knowledge unique to an organization", "C. Financial resources of a company", "D. Physical assets owned by a company"]', 
     "B"),
    ("Strategic Management", "What is BCG Matrix?", 
     '["A. Business Case Generation", "B. Balanced Capital Growth", "C. Boston Consulting Group", "D. Business Classification Graph"]', 
     "C"),
    ("Strategic Management", "What is Ansoff Matrix used for?", 
     '["A. Strategy evaluation", "B. Marketing analysis", "C. Product development planning", "D. Financial forecasting"]', 
     "C"),
    ("Strategic Management", "Define Competitive Advantage.", 
     '["A. Any factor that allows a company to differentiate its product or service", "B. Selling products at a lower price than competitors", "C. Maximizing profits", "D. Meeting customer expectations"]', 
     "A"),
    ("Strategic Management", "What is meant by Blue Ocean Strategy?", 
     '["A. Creating new market space", "B. Copying strategies of competitors", "C. Dominating existing markets", "D. Focusing on traditional marketing methods"]', 
     "A"),
    ("Strategic Management", "What is meant by Cost Leadership?", 
     '["A. Competing based on low costs", "B. Leading in terms of product quality", "C. Being innovative", "D. Focusing on niche markets"]', 
     "A"),
    ("Strategic Management", "What is meant by Differentiation Strategy?", 
     '["A. Offering unique features or benefits to customers", "B. Competing on price alone", "C. Focusing on a narrow market segment", "D. Following the market leader"]', 
     "A"),
]

# Digital Marketing questions
digital_marketing_questions = [
    ("Digital Marketing", "What is SEO?", 
     '["A. Search Engine Optimization", "B. Social Engagement Optimization", "C. Secure Email Operation", "D. Sales Engagement Opportunity"]', 
     "A"),
    ("Digital Marketing", "What is PPC?", 
     '["A. Pay Per Click", "B. Public-Private Collaboration", "C. Product Placement Cost", "D. Program Planning Cycle"]', 
     "A"),
    ("Digital Marketing", "What is the purpose of A/B testing in digital marketing?", 
     '["A. To measure website traffic", "B. To compare two versions of a webpage or app to determine which one performs better", "C. To create engaging social media posts", "D. To analyze competitors\' marketing strategies"]', 
     "B"),
    ("Digital Marketing", "What is the role of Key Performance Indicators (KPIs) in digital marketing?", 
     '["A. To measure the effectiveness of marketing campaigns", "B. To track employee attendance", "C. To manage inventory levels", "D. To forecast sales revenue"]', 
     "A"),
    ("Digital Marketing", "What is Email Marketing?", 
     '["A. Sending mass emails to random recipients", "B. Sending personalized emails to potential customers", "C. Creating email accounts for clients", "D. Managing corporate email servers"]', 
     "B"),
    ("Digital Marketing", "What is Content Marketing?", 
     '["A. Creating advertisements for television", "B. Creating valuable content to attract and engage an audience", "C. Producing low-quality content for quick distribution", "D. Selling digital products online"]', 
     "B"),
    ("Digital Marketing", "What is Social Media Marketing?", 
     '["A. Marketing through traditional media channels", "B. Marketing through online social platforms", "C. Marketing through direct mail", "D. Marketing through telephone calls"]', 
     "B"),
    ("Digital Marketing", "What is Influencer Marketing?", 
     '["A. Marketing to influential people within a company", "B. Marketing through celebrity endorsements", "C. Marketing through influential industry blogs", "D. Marketing through internal company influencers"]', 
     "B"),
    ("Digital Marketing", "What is SEM?", 
     '["A. Search Engine Marketing", "B. Social Engagement Management", "C. Secure Email Messaging", "D. Sales Efficiency Metrics"]', 
     "A"),
    ("Digital Marketing", "What is Remarketing?", 
     '["A. Marketing to existing customers", "B. Marketing to new customers", "C. Reusing old marketing materials", "D. Targeting users who previously visited a website"]', 
     "D"),
]

# Personal Sales questions
personal_sales_questions = [
    ("Personal Sales", "What is SPIN Selling?", 
     '["A. A sales technique", "B. A marketing campaign", "C. A management strategy", "D. A negotiation tactic"]', 
     "A"),
    ("Personal Sales", "What is the AIDA model?", 
     '["A. Attention, Interest, Desire, Action", "B. Awareness, Interest, Decision, Action", "C. Attract, Inform, Deliver, Assess", "D. Analysis, Interpretation, Development, Assessment"]', 
     "A"),
    ("Personal Sales", "What is the primary objective of a sales presentation?", 
     '["A. To inform potential customers about the company\'s history", "B. To persuade potential customers to buy a product or service", "C. To entertain potential customers with multimedia content", "D. To provide technical support to existing customers"]', 
     "B"),
    ("Personal Sales", "What is the importance of active listening in personal sales?", 
     '["A. To talk more effectively about the company\'s products", "B. To increase the volume of sales calls", "C. To understand the customer\'s needs and preferences", "D. To reduce the duration of sales meetings"]', 
     "C"),
    ("Personal Sales", "What is Consultative Selling?", 
     '["A. Selling products without customer interaction", "B. Selling products through a consultation process", "C. Selling products door-to-door", "D. Selling products through online platforms"]', 
     "B"),
    ("Personal Sales", "What is Relationship Selling?", 
     '["A. Building long-term relationships with customers", "B. Selling products to friends and family", "C. Selling products through social media", "D. Selling products through advertising"]', 
     "A"),
    ("Personal Sales", "What is the Challenger Sales Model?", 
     '["A. Challenging customers to buy products", "B. Challenging traditional sales methods", "C. Challenging customers\' assumptions and views", "D. Challenging competitors\' prices"]', 
     "C"),
    ("Personal Sales", "What is the Sandler Selling System?", 
     '["A. A sales training method", "B. A negotiation strategy", "C. A pricing model", "D. A marketing technique"]', 
     "A"),
    ("Personal Sales", "What is Needs-Based Selling?", 
     '["A. Identifying and fulfilling customer needs", "B. Focusing on product features", "C. Selling products based on personal needs", "D. Selling products at a low price"]', 
     "A"),
    ("Personal Sales", "What is Solution Selling?", 
     '["A. Selling solutions rather than products", "B. Selling products without understanding customer needs", "C. Selling products based on price alone", "D. Selling products through a bidding process"]', 
     "A"),
]

# Information Systems questions
information_systems_questions = [
    ("Information Systems", "What is ERP?", 
     '["A. Enterprise Resource Planning", "B. Electronic Reporting Process", "C. Efficient Resource Protocol", "D. Event Response Protocol"]', 
     "A"),
    ("Information Systems", "What is CRM?", 
     '["A. Customer Relationship Management", "B. Consumer Research Management", "C. Customer Response Management", "D. Consumer Relationship Management"]', 
     "A"),
    ("Information Systems", "What is the purpose of a firewall in information systems?", 
     '["A. To prevent unauthorized access to a network", "B. To speed up internet connectivity", "C. To store data securely", "D. To create virtual private networks"]', 
     "A"),
    ("Information Systems", "What is the role of a database management system (DBMS) in information systems?", 
     '["A. To design graphical user interfaces", "B. To manage and organize data efficiently", "C. To develop mobile applications", "D. To analyze market trends"]', 
     "B"),
    ("Information Systems", "What is SCM?", 
     '["A. Supply Chain Management", "B. Strategic Cost Management", "C. Service Contract Management", "D. Sales Channel Management"]', 
     "A"),
    ("Information Systems", "What is BI?", 
     '["A. Business Innovation", "B. Business Intelligence", "C. Balanced Integration", "D. Budget Implementation"]', 
     "B"),
    ("Information Systems", "What is E-commerce?", 
     '["A. Electronic Communication", "B. Electronic Commerce", "C. Effective Competition", "D. Efficient Collaboration"]', 
     "B"),
    ("Information Systems", "What is Data Mining?", 
     '["A. Extracting useful information from large datasets", "B. Mining minerals for manufacturing", "C. Extracting data from databases", "D. Extracting data from websites"]', 
     "A"),
    ("Information Systems", "What is Data Warehousing?", 
     '["A. Storing data for long-term use", "B. Storing data for short-term use", "C. Deleting old data", "D. Selling data to third parties"]', 
     "A"),
    ("Information Systems", "What is IT Governance?", 
     '["A. Frameworks and processes for decision-making", "B. Oversight of hardware and software", "C. Managing IT projects", "D. Implementing IT security measures"]', 
     "A"),
]

# Project Management questions
project_management_questions = [
    ("Project Management", "What is PERT?", 
     '["A. Program Evaluation and Review Technique", "B. Project Efficiency and Resource Tracking", "C. Project Execution and Reporting Tool", "D. Programmatic Event Recognition Technology"]', 
     "A"),
    ("Project Management", "What is Gantt Chart?", 
     '["A. A visual project management tool", "B. A financial statement analysis tool", "C. A quality management technique", "D. A risk assessment method"]', 
     "A"),
    ("Project Management", "What is Risk Management in project management?", 
     '["A. Identifying, assessing, and mitigating risks that could impact project objectives", "B. Managing team members\' schedules", "C. Assigning tasks to team members", "D. Analyzing project budget"]', 
     "A"),
    ("Project Management", "What is a Work Breakdown Structure (WBS)?", 
     '["A. A hierarchical decomposition of the total scope of work to be carried out by the project team", "B. A schedule of team meetings", "C. A document outlining project goals", "D. A plan for project execution"]', 
     "A"),
    ("Project Management", "What does the Critical Path Method (CPM) determine in project management?", 
     '["A. The longest sequence of dependent tasks and their durations", "B. The total budget of the project", "C. The number of team members needed for the project", "D. The project\'s success rate"]', 
     "A"),
    ("Project Management", "What is Resource Leveling in project management?", 
     '["A. Adjusting the project schedule to ensure that resources are not overallocated", "B. Reducing the number of resources assigned to the project", "C. Increasing the project duration to accommodate more resources", "D. Prioritizing resources over project tasks"]', 
     "A"),
    ("Project Management", "What is Earned Value Management (EVM)?", 
     '["A. A project management technique for measuring project performance and progress", "B. A method for assigning value to project deliverables", "C. A strategy for acquiring project resources", "D. A tool for project risk assessment"]', 
     "A"),
    ("Project Management", "What is a Change Control Board (CCB) responsible for in project management?", 
     '["A. Evaluating and approving or rejecting changes to the project scope, schedule, or cost", "B. Managing project team meetings", "C. Creating project reports", "D. Developing the project budget"]', 
     "A"),
    ("Project Management", "What is Scope Creep in project management?", 
     '["A. The uncontrolled expansion of project scope without adjustments to time, cost, and resources", "B. The formal acceptance of project deliverables", "C. The process of defining project objectives", "D. The completion of project milestones ahead of schedule"]', 
     "A"),
    ("Project Management", "What is Quality Assurance in project management?", 
     '["A. The planned and systematic activities implemented within the quality system to provide confidence that the project will satisfy quality requirements", "B. The inspection of project documents", "C. The completion of project tasks", "D. The management of project risks"]', 
     "A"),
]

# Insert data into the database
for question in strategic_management_questions:
    category, question_text, options_str, correct_answer = question
    options_list = eval(options_str)  # Parse the string into a list
    options_str = json.dumps(options_list)  # Convert list to JSON string
    c.execute('''INSERT INTO questions (category, question, options, correct_answer) 
                 VALUES (?, ?, ?, ?)''', (category, question_text, options_str, correct_answer))
    
for question in digital_marketing_questions:
    category, question_text, options_str, correct_answer = question
    options_list = eval(options_str)  # Parse the string into a list
    options_str = json.dumps(options_list)  # Convert list to JSON string
    c.execute('''INSERT INTO questions (category, question, options, correct_answer) 
                 VALUES (?, ?, ?, ?)''', (category, question_text, options_str, correct_answer))

for question in personal_sales_questions:
    category, question_text, options_str, correct_answer = question
    options_list = eval(options_str)  # Parse the string into a list
    options_str = json.dumps(options_list)  # Convert list to JSON string
    c.execute('''INSERT INTO questions (category, question, options, correct_answer) 
                 VALUES (?, ?, ?, ?)''', (category, question_text, options_str, correct_answer))

for question in information_systems_questions:
    category, question_text, options_str, correct_answer = question
    options_list = eval(options_str)  # Parse the string into a list
    options_str = json.dumps(options_list)  # Convert list to JSON string
    c.execute('''INSERT INTO questions (category, question, options, correct_answer) 
                 VALUES (?, ?, ?, ?)''', (category, question_text, options_str, correct_answer))

for question in project_management_questions:
    category, question_text, options_str, correct_answer = question
    options_list = eval(options_str)  # Parse the string into a list
    options_str = json.dumps(options_list)  # Convert list to JSON string
    c.execute('''INSERT INTO questions (category, question, options, correct_answer) 
                 VALUES (?, ?, ?, ?)''', (category, question_text, options_str, correct_answer))

# Commit changes and close the connection
conn.commit()
conn.close()
