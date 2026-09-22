# -*- coding: utf-8 -*-
# Slide model for "A Look at the Present and Future of Robotics" (EN, Sep 2026)
# kind: cover | agenda | quote | bullets | anchor | data | chart | video | breath | close
S = [
dict(kind="cover", title="A Look at the Present<br>and Future of Robotics",
     who="Javier Fuentes Ibáñez", org="NCompany", date="Madrid · 24 September 2026", art="golem"),

dict(kind="agenda", title="The road"),

# ---------------- ACT I — THE OLD LONGING ----------------
dict(kind="quote", act="The old longing",
     text="“…so much like men, and men so much like robots, that eventually we'll lose the distinction altogether.”",
     src="Isaac Asimov, BBC <i>Towards Tomorrow</i>, 1967"),

dict(kind="video", act="The old longing", title="The question is sixty years old",
     vid="_7_DiUpyrjc", slug="01-asimov-1967", label="1967: Can Humans and Robots Co-Exist? · BBC Archive"),

dict(kind="bullets", act="The old longing", title="Talos", art="talos", items=[
  "bronze giant, forged by a god, patrolling Crete three times a day",
  "the first automaton in the Western imagination",
  "already the two obsessions: tireless labour and absolute obedience",
  "and already the flaw: a single bronze nail at the ankle"]),

dict(kind="bullets", act="The old longing", title="Pandora", art="pandora", items=[
  "made, not born. assembled by Hephaestus on commission",
  "depicted on Greek pottery around 460 BC",
  "the artificial being arrives as a gift and as a punishment",
  "we have never told this story neutrally"]),

dict(kind="bullets", act="The old longing", title="The Golem", art="golem", items=[
  "the legend of Prague: clay shaped into a servant by Rabbi Loew",
  "animated by a word placed in its mouth. take the word out, and it is clay again",
  "set in the 1500s, written down in the 1800s, made famous by Meyrink's 1915 novel",
  "it does not rebel. it does exactly what it was told"]),

dict(kind="anchor", act="The old longing", dark=True,
     text="The Golem never disobeys.<br>That is the whole problem."),

dict(kind="bullets", act="The old longing", title="The right word", art="capek", items=[
  "<b>robot</b> comes from the Czech <i>robota</i>: forced labour",
  "coined by Karel Čapek in his 1920 play <i>R.U.R.</i>",
  "in the play the robots are organic, built to work, and they revolt",
  "we named the machine after the servitude, not the mechanism"]),

dict(kind="anchor", act="The old longing", wide=True,
     text="Three thousand years of wanting it.<br>Sixty years of it working behind a fence.<br>Three years of it starting to understand."),

# ---------------- ACT II — WHERE WE ACTUALLY ARE ----------------
dict(kind="bullets", act="Where we are", title="What a robot is today", art="arm", items=[
  "<b>industrial</b>: bolted down, fenced off, one task, decades of service",
  "<b>service</b>: mobile, among people, many tasks, short life",
  "arms build cars; wheels, legs and tracks come to you; drones go where you cannot",
  "almost everything profitable today is still the first kind"]),

dict(kind="data", act="Where we are", figure="542,000",
     cap="industrial robots installed worldwide in a single year",
     src="IFR, World Robotics 2025 · reporting year 2024", dark=True),

dict(kind="chart", act="Where we are", title="Where the robots went",
     years=list(range(2011, 2025)), highlight="China",
     series={
       "China":         [23000,23000,37000,57000,69000,97000,156000,155000,148000,178000,268000,290000,276000,295000],
       "Japan":         [28000,29000,25000,29000,35000,39000,46000,55000,50000,39000,47000,50000,46000,45000],
       "United States": [21000,22000,24000,26000,28000,31000,33000,40000,33000,31000,35000,40000,38000,34000],
       "South Korea":   [26000,19000,21000,25000,38000,41000,40000,38000,33000,31000,31000,32000,31000,31000],
       "Germany":       [20000,18000,18000,20000,20000,20000,21000,27000,22000,22000,24000,26000,28000,27000]},
     note="295,000 in 2024, thirteen times 2011",
     src="IFR World Robotics, via Our World in Data · new industrial robots installed per year, 2011–2024"),

dict(kind="bullets", act="Where we are", title="How to read that number", items=[
  "operational stock worldwide: <b>4.66 million</b> robots, up 9%",
  "China took <b>54%</b> of everything installed that year",
  "Asia 74% · Europe 16% · Americas 9%",
  "Chinese domestic suppliers now hold 57% of their own market",
  ], src="IFR, World Robotics 2025"),

dict(kind="data", act="Where we are", figure="1,220 vs 132",
     cap="robots per 10,000 manufacturing workers: South Korea against the world average",
     src="IFR robot density, published April 2026 · reporting year 2024", map="KOR"),

dict(kind="bullets", act="Where we are", title="Italy and Spain", items=[
  "<b>Italy: 8,783</b> robots installed in 2024, down 16% – still second in Europe, fifth in the world",
  "<b>Spain: 5,160</b>, up 2% – third in Europe, ahead of France for the first time since 2015",
  "density per 10,000 workers: Italy 228, EU average 231, Germany 449",
  "Italy's drop was domestic: a year spent waiting for the Transizione 5.0 incentives"],
  src="IFR World Robotics 2025, Sept 2025 · IFR density, April 2026 · SIRI–UCIMU, Feb 2025 · AER Automation, July 2025"),

# ---------------- ACT III — THE EXPECTATION GAP ----------------
dict(kind="bullets", act="The gap", title="Unmet expectations", art="automaton", items=[
  "the future we were promised: a humanoid servant in every home",
  "the future we got: a sealed arm welding the same seam for twenty years",
  "we mistook the <b>shape</b> of the machine for the point of it",
  "for fifty years robots were strong, fast, precise – and blind"]),

dict(kind="anchor", act="The gap", text="Slowly.<br>And then suddenly."),

# ---------------- ACT IV — AI MEETS ROBOTICS ----------------
dict(kind="bullets", act="AI meets robotics", title="2023", art="brain-gear", items=[
  "RT-2: the first model to read the web and output robot actions",
  "success on <b>unseen</b> scenarios rose from 32% to 62%",
  "impressive – and it all happened inside one office kitchen",
  "generalisation meant new objects, not a new building"],
  src="Google DeepMind, RT-2, July 2023"),

dict(kind="video", act="AI meets robotics", title="Pick up the extinct animal",
     link="https://robotics-transformer2.github.io/", slug="09-rt2-2023",
     label="RT-2 demonstrations · Google DeepMind, July 2023 · silent footage"),

dict(kind="bullets", act="AI meets robotics", title="2026", art="stage-mud", items=[
  "one frozen model walked into <b>30 homes it had never seen</b>",
  "tidy the living room, fold the towels, make the bed",
  "no data from those homes, no retraining, unseen objects",
  "<b>56%</b> of the tasks done, first time, no help"],
  src="Figure, Helix 2.5, September 2026 · company-reported"),

dict(kind="video", act="AI meets robotics", title="Thirty homes, one model",
     vid="lJpM_2a1zrE", slug="10-figure-helix-25", label="Helix 2.5: 30-Home Generalization · Figure, September 2026"),

dict(kind="data", act="AI meets robotics", figure="56%",
     cap="an extraordinary research result. and a product number no plant manager would accept",
     src="Figure, Helix 2.5, September 2026 · company-reported"),

dict(kind="video", act="AI meets robotics", title="Reasoning before acting",
     vid="UObzWjPb6XM", slug="02-gemini-robotics", label="Gemini Robotics 1.5 · Google DeepMind, September 2025"),

dict(kind="anchor", act="AI meets robotics", dark=True,
     text="Robots stopped being programmed.<br>They started being trained."),

dict(kind="bullets", act="AI meets robotics", title="Live: a word in its mouth", art="reachy-mini", items=[
  "<b>Reachy Mini</b>: Pollen Robotics and Hugging Face. open source, $299",
  "four microphones, a camera, a speaker. no arms, no legs",
  "voice mode: it listens, a model answers, the body reacts",
  "watch the pauses and the misreadings. that is the work left"],
  src="Hugging Face · Pollen Robotics, Reachy Mini launch, July 2025 · live, unscripted"),

dict(kind="bullets", act="AI meets robotics", title="Skills now move between bodies", art="hand-word", items=[
  "a skill learned on one arm transfers to a different robot entirely",
  "no re-engineering, no per-platform specialisation",
  "a model folded a shirt on a bimanual arm it had never trained on",
  "the skill stopped being a property of the machine"],
  src="DeepMind Motion Transfer, Sep 2025 · Physical Intelligence π0.7, Apr 2026"),

dict(kind="video", act="AI meets robotics", title="Eight hours of demonstrations",
     vid="f6ChFc8eUuo", slug="03-figure-helix", label="Helix Logistics · Figure, February 2025"),

dict(kind="data", act="AI meets robotics", figure="$90,000 → $29,900",
     cap="what a full-size humanoid cost, April 2024 against October 2025",
     src="Unitree H1 and H2 list prices", dark=True),

dict(kind="bullets", act="AI meets robotics", title="The research bench collapsed too", art="scale", items=[
  "2023: ALOHA, a capable bimanual rig, under <b>$20,000</b>",
  "2026: an SO-101 leader-follower pair, around <b>€550</b>",
  "a 450M-parameter policy trains on one consumer GPU",
  "the barrier to trying this is now a rounding error"],
  src="ALOHA, Apr 2023 · LeRobot, Feb 2026"),

dict(kind="video", act="AI meets robotics", title="And the volume is Chinese",
     vid="eUdBIFkMh-M", slug="04-unitree-h2", label="Unitree H2 · Unitree Robotics, October 2025"),

dict(kind="bullets", act="AI meets robotics", title="Bigger is not the answer on a robot", art="pocketwatch", items=[
  "an 81B-parameter policy runs at <b>9.6 Hz</b> – on a datacentre GPU",
  "a robot arm needs 50 Hz, on hardware that fits inside it, at 40 watts",
  "a 450M model matches ones ten times its size on real tasks",
  "and fine-tuning to <b>your</b> task beats a generalist cold: 43.7% vs 17.7%"],
  src="VLA-Perf, Feb 2026 · SmolVLA, Jun 2025 · RoboChallenge, Oct 2025"),

dict(kind="data", act="AI meets robotics", figure="89.4% → 12.4%",
     cap="best success on 18 short tabletop tasks, then on 1,000 long household chores. both in simulation",
     src="Stanford AI Index 2026 · RLBench, EquAct, January 2026 · BEHAVIOR-1K Challenge, 2025, top team"),

dict(kind="bullets", act="AI meets robotics", title="And they are slow", items=[
  "package sorting: <b>4× slower</b> than an average worker",
  "laundry 5× slower; most household tasks 2–10× slower than a person",
  "nudge the camera and benchmark scores fall from 95% to under 30%",
  "what is genuinely in production: a warehouse picker, a truck unloader, an underwater drone. no humanoid"],
  src="Epoch AI, Where Autonomy Works, February 2026 · LIBERO-Plus, CVPR 2026"),

dict(kind="video", act="AI meets robotics", title="What autonomy looks like",
     vid="F_7IPm7f1vI", slug="05-atlas-hands-on", label="Atlas Goes Hands On · Boston Dynamics – no teleoperation"),

dict(kind="video", act="AI meets robotics", title="And what it does not",
     vid="LTYMWadOW7c", slug="06-1x-neo", label="NEO The Home Robot · 1X – shipped with human teleoperators in the loop"),

dict(kind="anchor", act="AI meets robotics",
     text="Ask for the intervention rate.<br>Ask for the hours. Ask for the site."),

# ---------------- ACT V — WHAT WORKED, WHAT DIDN'T ----------------
dict(kind="bullets", act="Evidence", title="The best-evidenced deployment there is", art="factory", items=[
  "Figure 02 at BMW Spartanburg, eleven months, ten-hour shifts",
  "<b>1,250 hours</b> of runtime, <b>90,000 parts</b> loaded onto welding fixtures",
  "99% placement accuracy at 5 mm tolerance, 84-second cycle",
  "one task. one fixture. one plant"],
  src="Figure and BMW Group, 2025 · corroborated in Stanford AI Index 2026"),

dict(kind="video", act="Evidence", title="See it before you judge it",
     vid="xLVm-QKEZSI", slug="07-bmw-figure", label="Figure 02 at BMW Group Plant Spartanburg · BMW Group"),

dict(kind="bullets", act="Evidence", title="And then it came back", items=[
  "the retired fleet was scratched, scuffed and grimy",
  "the recurring hardware failure was the forearm",
  "this is what a real deployment looks like at the end",
  "every demo you have ever seen was filmed on day one"],
  src="Figure, November 2025"),

dict(kind="bullets", act="Evidence", title="The same eighteen months, the other column", items=[
  "Amazon's Blue Jay sortation system: launched October, shut down by February",
  "Tesla, January 2026: Optimus is \"not in usage in our factories in a material way\"",
  "Agility's Digit at Amazon: still a pilot, three years in",
  "Rethink Robotics, iRobot, K-Scale: bankrupt or wound down"],
  src="The Robot Report, Reuters, company statements 2025–2026"),

dict(kind="data", act="Evidence", figure="22,000",
     cap="humanoid robots shipped in the first half of 2026: up nearly 300%, and 86% from Chinese vendors",
     src="Counterpoint Research, 20 August 2026", dark=True),

dict(kind="video", act="Evidence", title="Meanwhile, the revolution that already happened",
     vid="7SvTdW4OLUQ", slug="08-amazon-robots", label="The full Amazon robot line-up · Amazon News – one million robots deployed"),

# ---------------- ACT VI — BUSINESS IMPACT ----------------
dict(kind="bullets", act="Business impact", title="Three levels, not one", items=[
  "<b>operational</b>: what the machine can actually do, and how often it fails",
  "<b>financial</b>: how you pay for it, and when it pays you back",
  "<b>labour</b>: who does what afterwards, and who says so",
  "most boards only ever discuss the first one"]),

dict(kind="bullets", act="Business impact", title="From CapEx to OpEx", art="lease-cart", items=[
  "you are no longer buying a machine. you are buying hours",
  "Robot-as-a-Service revenue grew <b>31%</b> in one year",
  "GXO signed the first multi-year humanoid RaaS contract in 2024",
  "no vendor publishes an hourly rate. ask for one in writing"],
  src="IFR Service Robots 2025 · GXO, June 2024"),

dict(kind="bullets", act="Business impact", title="Numbers to calibrate the answer", art="steam", items=[
  "an industrial arm pays back in <b>18–36 months</b>; a cobot cell in 12–18",
  "Digit, by Agility: about <b>$8,500 a month</b>, plus $25,000 to deploy",
  "its own yardstick: a fully loaded worker at <b>$30 an hour</b>",
  "labour per hour, 2025: Italy €32 · Spain €26 · Germany €45 · EU €35"],
  src="integrator benchmarks 2026 · Agility Robotics investor deck, June 2026 · The Robot Report · Eurostat, March 2026"),

dict(kind="bullets", act="Business impact", title="Labour: the honest version", items=[
  "the famous US study: one more robot per thousand workers costs <b>about 6 jobs</b> locally, 3 nationally",
  "the 2025 meta-analysis of 33 studies: average effect <b>−0.02</b>. negligible",
  "strongly negative in the United States, <b>positive</b> in other developed economies",
  "the effect is not a law of physics. it is a policy outcome"],
  src="Acemoglu & Restrepo, JPE 2020 · Guarascio et al., J. Econ. Surveys 2025"),

dict(kind="bullets", act="Business impact", title="And the shortage is real", art="fishing-net", items=[
  "welders are in shortage in <b>22</b> European countries",
  "plumbers in 20, electricians in 21, heavy vehicle mechanics in 16",
  "US manufacturing: <b>1.9 million</b> roles projected unfilled by 2033",
  "the question is not whether to automate. it is what, and in which order"],
  src="EURES Labour Shortages Report 2025 · Deloitte & The Manufacturing Institute, 2024"),

dict(kind="bullets", act="Business impact", title="Follow the money", items=[
  "OpenAI lists <b>27</b> robotics jobs, up from 11 in May. base pay $177,000 to $500,000",
  "the best-paid role never touches a robot: it builds the training-data pipeline",
  "the rest: actuator design, data-acquisition stations, a manager for data collection",
  "the top lab treats robotics as a data problem. so should your budget"],
  src="Business Insider, 18 September 2026 · OpenAI careers page · The Next Web"),

dict(kind="bullets", act="Business impact", title="One date for your calendar", art="seal", items=[
  "the EU Machinery Regulation applies from <b>20 January 2027</b>",
  "it replaces the 2006 Machinery Directive and covers AI in safety functions",
  "the AI Act's machinery obligations were deferred to August 2028",
  "the nearer deadline is the one nobody is talking about"],
  src="Regulation (EU) 2023/1230 · EU Digital Omnibus, May 2026"),

# ---------------- ACT VII — UNCOMFORTABLE CONCLUSIONS ----------------
dict(kind="anchor", act="Uncomfortable conclusions", kicker="Uncomfortable conclusion 1", dark=True,
     text="The hardware got cheap.<br>The competence did not."),

dict(kind="anchor", act="Uncomfortable conclusions", kicker="Uncomfortable conclusion 2",
     text="The robot that pays for itself<br>in your plant is not humanoid."),

dict(kind="anchor", act="Uncomfortable conclusions", kicker="Uncomfortable conclusion 3", dark=True,
     text="The bottleneck is data,<br>and your operation is where it lives."),

dict(kind="breath", act="Uncomfortable conclusions", art="warehouse"),

# ---------------- ACT VIII — MONDAY ----------------
dict(kind="bullets", act="On Monday", title="Pick a task, not a robot", items=[
  "write down the five tasks that cost you most in overtime and injuries",
  "score each one: is it repetitive, is the part always in the same place",
  "the winner is usually dull, dirty and already measured",
  "buy for that task. not for the press release"]),

dict(kind="bullets", act="On Monday", title="Buy hours, not machines", items=[
  "structure the first deployment as a service, with an exit",
  "tie payment to a metric you already track: parts per hour, tote accuracy",
  "agree who pays when it fails, before it fails",
  "a two-year commitment on this technology is a long time"]),

dict(kind="bullets", act="On Monday", title="Start recording now", items=[
  "the models are short of data about <b>your</b> process, not about the world",
  "that is why 1X ships NEO with humans in the loop: every shift is training data",
  "video, cycle times, failure modes, the operator's hands: cheap today, unbuyable later",
  "whoever holds the task data holds the negotiating position"]),

dict(kind="bullets", act="On Monday", title="Demand three numbers", items=[
  "<b>hours</b> of unattended operation, at a named site",
  "<b>intervention rate</b>: how often a human had to step in",
  "<b>cycle time</b> against your current human baseline",
  "a vendor who cannot give you all three is selling a film"]),

# ---------------- CLOSE ----------------
dict(kind="bullets", act="Close", title="Back to the Golem", art="hand-word", items=[
  "the clay was never the hard part. the word was",
  "it obeyed exactly what was written, which is why it had to be stopped",
  "we are about to hand instructions to machines that execute them literally",
  "the engineering problem is solved faster than the instruction problem"]),

dict(kind="close", title="Thank you", mail="javier@ncompany.es", who="Javier Fuentes Ibáñez", org="NCompany"),
]
