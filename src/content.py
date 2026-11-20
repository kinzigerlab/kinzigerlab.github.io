"""Content for the Kinziger Lab site.

Everything a lab member would normally edit lives in this file:
PEOPLE, ALUMNI, PUBLICATIONS and the page text.
After editing, run:  python3 build.py

Tiny markup used in text fields:  *italic*   **bold**   [label](url)
"""

DC = "https://digitalcommons.humboldt.edu/etd/"

# --------------------------------------------------------------------------
# HOME
# --------------------------------------------------------------------------
HERO = {
    "h1": "Environmental DNA and conservation genetics of fishes",
    "lede": (
        "We are a research lab in the Department of Fisheries Biology at Cal Poly Humboldt. "
        "We detect fish from the DNA they leave in water, and we use genetic data to guide the "
        "conservation of salmon, lamprey, tidewater goby and other fishes of California's North Coast."
    ),
}

LABEL = [  # the small fact label beside the hero
    ("Location", "Arcata, California"),
    ("Lab lead", "Andrew Kinziger, Professor and Chair"),
    ("M.S. graduates", None),   # filled in from ALUMNI by build.py
]

# Photographs.  "src" is a file in site/img/.  "where" is set in italic like the place names;
# "note" text shows only in the draft.
HOME_PHOTO = {
    "src": "lake-earl-2007.jpg", "w": 2000, "h": 1500,
    "alt": "Two researchers in chest waders pull a seine net through the reedy shallows of a coastal lagoon.",
    "where": "Lake Earl, Del Norte County",
    "caption": "Pulling a seine through the lagoon shallows, June 2007.",
    "credit": "Kinziger Lab",
}

WORKFLOW_INTRO = (
    "Fish shed cells into the water around them. A water sample carries enough of their DNA "
    "to show which species are present, without netting or handling a fish."
)
WORKFLOW = [
    ("Collect", "One or two liters of water from a river, lagoon or bay, with replicate samples at each site."),
    ("Filter", "The water passes through a fine filter that traps cells and loose DNA. Filters are frozen or preserved in the field."),
    ("Extract", "DNA is purified from each filter in a clean lab, alongside blanks that would reveal contamination."),
    ("Amplify", "qPCR targets a single species. Metabarcoding copies a short gene from every fish in the sample and sequences them all."),
    ("Interpret", "Occupancy models use the replicate samples to estimate how likely we were to miss a species that was there."),
]
PRIMER = ("GTCGGTAAAACTCGTGCCAGC", "MiFish-U forward primer for the 12S gene")

PILLARS = [
    {
        "key": "edna",
        "title": "Environmental DNA",
        "text": (
            "We develop eDNA methods and put them to work in monitoring programs: endangered tidewater goby "
            "along the whole California coast, salmon returning to the Klamath River after dam removal, "
            "coho salmon in small streams, and entire fish communities from Humboldt Bay to the ocean offshore."
        ),
        "link": ("eDNA research", "#edna"),
    },
    {
        "key": "gen",
        "title": "Conservation genetics and genomics",
        "text": (
            "We use genetic data to find the genes behind salmon run timing and lamprey life histories, "
            "to measure how isolated small populations are, to trace where introduced fishes came from, "
            "and to evaluate hatchery programs."
        ),
        "link": ("Genetics research", "#genetics"),
    },
]

# Rivers, lagoons and bays run north to south; the two coastwide entries come last.  tags: "edna", "gen"
PLACES = [
    ("Smith River", "Coho salmon surveys by eDNA, and an introduced population of Klamath smallscale sucker traced to its source.", ["edna", "gen"], ""),
    ("Klamath River", "Daily eDNA sampling at the former Iron Gate Dam site follows salmon and steelhead back into the upper basin, and eDNA metabarcoding in the estuary watches for aquatic invasive species. Genetics of Pacific lamprey, Chinook salmon and speckled dace.", ["edna", "gen"], ""),
    ("Trinity River", "Spring-run and fall-run Chinook salmon, and the genetics of run timing.", ["gen"], ""),
    ("Big Lagoon and the North Coast lagoons", "Endangered tidewater goby: population genetics, field tests of eDNA methods, and a yearly population estimate at Big Lagoon.", ["edna", "gen"], ""),
    ("Mad River", "More than four decades of hatchery steelhead, read through their genetics.", ["gen"], ""),
    ("Humboldt Bay", "A year of water samples, taken every two weeks, detected 97 fish species.", ["edna"], ""),
    ("Eel River", "Where introduced Sacramento pikeminnow came from, and eDNA surveys of the headwaters ahead of dam removal.", ["edna", "gen"], ""),
    ("The California coast", "Coastwide eDNA surveys of lagoons and estuaries for tidewater goby, along the length of the state, and metabarcoding of fish communities in ocean habitats near shore.", ["edna"], ""),
    ("Offshore wind energy areas", "Water sampled at depth on survey cruises aboard R/V North Wind, for a baseline of the fish community in the Humboldt Wind Energy Area.", ["edna"], ""),
]
PLACES_SUB = "Rivers, lagoons and bays from north to south, then the coast as a whole and the ocean offshore."
PLACES_NOTE = ""

# --------------------------------------------------------------------------
# RESEARCH
# --------------------------------------------------------------------------
RESEARCH_INTRO = (
    "We use DNA to answer practical questions about fishes: where a species lives, how many there are, "
    "how its populations are connected and what sets them apart. Most of the work is on California's "
    "North Coast, alongside the agencies, Tribes and organizations that manage these fish."
)

CURRENT = [
    "Daily eDNA sampling on the Klamath River at the former Iron Gate Dam site",
    "Early detection of aquatic invasive species in the Klamath River estuary, pairing eDNA metabarcoding with conventional sampling",
    "Fish community metabarcoding in Humboldt Bay and North Coast estuaries",
    "Fish eDNA on the offshore surveys of the Humboldt Wind Energy Area, aboard R/V North Wind",
    "Sacramento pikeminnow and rainbow trout distribution in the upper Eel River ahead of dam removal",
    "Sampling design and field-workflow tests for tidewater goby eDNA",
    "Reference sequences for northern California fishes",
    "eDNA detection of non-natal Chinook rearing in the Sacramento River",
]
CURRENT_NOTE = ""

EDNA_LEDE = (
    "Fish leave DNA in the water. We filter it out, read it, and use it to find species without netting, "
    "snorkeling or handling a single fish. For more than a decade the lab has tested how well that works "
    "and built it into monitoring programs."
)

# The lab sequence shown under the eDNA heading.  "step" uses the same words as the home page diagram.
EDNA_STRIP = {
    "photos": [
        {"src": "lab-filter-2026.jpg", "w": 1200, "h": 800, "step": "Filter",
         "alt": "At a lab bench beside a window, a student in blue gloves pours a water sample from a bag into a filter funnel on a vacuum manifold."},
        {"src": "lab-pcr-setup-2026.jpg", "w": 1200, "h": 800, "step": "Extract and prepare",
         "alt": "Seen through the glass front of a PCR hood, a gloved student holds a repeating pipette over a 96-well plate."},
        {"src": "lab-qpcr-2026.jpg", "w": 1200, "h": 800, "step": "Amplify",
         "alt": "A student holds a sealed 96-well plate at the open tray of a QuantStudio 3 qPCR instrument while a second student looks on."},
    ],
    "caption": (
        "Levy Young filters water samples to capture eDNA, performs DNA extraction and qPCR preparation in a "
        "dedicated PCR hood and, with Joey Salazar, loads a prepared plate into the QuantStudio 3 qPCR instrument. "
        "Both were Fisheries Biology undergraduates working in the lab. June 2026."
    ),
    "credit": "Kellie Jo Brown, Cal Poly Humboldt",
}

D = "https://doi.org/"
EDNA_TOPICS = [
    {
        "title": "Tidewater goby along the whole California coast",
        "figure": {
            "src": "tidewater-goby.jpg", "w": 1400, "h": 603,
            "alt": "A tidewater goby, a small mottled olive fish with two dorsal fins, resting on the bottom of a clear photo tank.",
            "where": "",
            "caption": "A tidewater goby (*Eucyclogobius newberryi*) in a field photo tank.",
            "credit": "Kinziger Lab",
        },
        "body": [
            "The endangered tidewater goby lives in coastal lagoons and estuaries, where surveys with nets are slow "
            "and can miss it. We designed a qPCR assay for the species and showed that water samples detect gobies "
            "nearly twice as reliably as seining. We then surveyed roughly 200 sites along all 1,350 km of the "
            "California coast, and repeated the survey a year later to estimate how often goby populations wink "
            "out and recolonize.",
            "Current work asks how many water samples a site needs and compares field filtration systems side by "
            "side. Alongside the eDNA work, we have estimated the size of the Big Lagoon population by mark and "
            "recapture every year since 2008.",
        ],
        "refs": [
            ("Schmelzle and Kinziger 2016", D + "10.1111/1755-0998.12501"),
            ("Sutter and Kinziger 2019", D + "10.1007/s10592-019-01161-9"),
            ("Martel et al. 2021", D + "10.1111/mec.15693"),
        ],
    },
    {
        "title": "Salmon returning to the Klamath after dam removal",
        "figure": {
            "src": "klamath-edna-sampler-2026.jpg", "w": 1600, "h": 1067,
            "alt": "Three people in life jackets stand on a pontoon in a river beside an open equipment case; one holds up a bag of filters while the other two listen.",
            "where": "Klamath River",
            "caption": (
                "The autonomous eDNA sampler pumps and filters water continuously, collecting and preserving genetic "
                "material shed by fish and other aquatic organisms for later analysis. Graduate student Laura Redfield "
                "(left) teaches undergraduates Joey Salazar (center) and Heleen Mittry (right) the sampler's weekly "
                "filter change, June 2026."
            ),
            "credit": "Kinziger Lab",
        },
        "body": [
            "Four dams came off the Klamath River in 2024. An automated sampler near the former Iron Gate Dam site "
            "has collected and preserved water every day for more than a year. We run qPCR and metabarcoding on "
            "those samples to follow Chinook salmon, coho salmon and steelhead as they move into habitat that was "
            "closed to them for more than a century.",
            "Earlier Klamath projects tested whether eDNA can track the number of Chinook smolts leaving the river, "
            "and measured how unevenly eDNA from salmon and from the parasite *Ceratonova shasta* is spread across "
            "a large river channel. We are also developing methods that may one day tell spring-run from fall-run "
            "Chinook in a water sample.",
            "In the estuary, a project with José Marin Jarrin's lab pairs eDNA metabarcoding with conventional "
            "sampling to detect aquatic invasive species early.",
        ],
        "refs": [
            ("A River in Recovery, Humboldt magazine, fall 2026", "https://now.humboldt.edu/magazine/fall2026/klamath-river-restoration.html"),
            ("Coyne 2021 (thesis)", DC + "494"),
            ("Keel 2023 (thesis)", DC + "641"),
        ],
    },
    {
        "title": "Coho salmon in small streams",
        "body": [
            "Coho salmon are protected in California, and surveys for them are usually done by snorkeling. In the "
            "Smith River basin, eDNA and snorkel surveys agreed on whether coho were present in 93% of pools. "
            "A four-year project for Caltrans measured how quickly fish eDNA is shed and breaks down, and released "
            "DNA tracers into streams to learn how far a signal travels before it fades.",
        ],
        "refs": [
            ("Shaffer et al. 2024", D + "10.1002/nafm.10993"),
            ("Bandy 2024 (thesis)", DC + "727"),
            ("Caltrans final report, 2023", "https://rosap.ntl.bts.gov/view/dot/74442"),
        ],
    },
    {
        "title": "Whole fish communities from a bottle of water",
        "body": [
            "Metabarcoding copies a short stretch of the 12S gene from every fish in a sample and sequences them "
            "together. Water collected at one Humboldt Bay site every two weeks for a year held DNA from 97 fish "
            "species. That is more than any of four conventional surveys of the bay recorded, and 35 of the species "
            "had not turned up in those surveys at all.",
            "A companion project, part of Tribal Fisheries Resilience at Cal Poly Humboldt, sampled twelve marine "
            "and estuary sites along 168 km of the North Coast every month for a year. To keep identifications "
            "reliable, we are sequencing reference DNA from northern California fishes.",
            "Farther out, we sample by depth on survey cruises in the Humboldt Wind Energy Area to build a baseline "
            "of the fish community there.",
        ],
        "refs": [
            ("Richardson 2025 (thesis)", DC + "2533"),
            ("Tribal Fisheries Resilience eDNA project", "https://www.humboldt.edu/tribal-fisheries-resilience/edna"),
        ],
    },
    {
        "title": "Making eDNA dependable in the field",
        "body": [
            "A method is only useful if a field crew can run it the same way every time. We test the practical "
            "details: how many samples to take, which filter to use, and how long a sample survives before it "
            "reaches the lab. Self-preserving filters, for example, kept goby DNA detectable for more than two "
            "weeks at 33 °C but lost it quickly at 43 °C.",
        ],
        "refs": [
            ("Boche 2026 (thesis)", DC + "2554"),
            ("Keel 2023 (thesis)", DC + "641"),
            ("Bandy 2024 (thesis)", DC + "727"),
        ],
    },
]

GEN_LEDE = (
    "Genetic data show what a field survey cannot: which populations are isolated, which are mixing, where an "
    "introduced fish came from, and which genes underlie the traits that managers care about."
)

GEN_TOPICS = [
    {
        "title": "The genes behind run timing and life history",
        "body": [
            "Whether a Chinook salmon returns to the river in spring or fall comes down to one small region of its "
            "genome. That result, published in *Science* in 2020, matters for restoring spring-run fish to the upper "
            "Klamath. Pacific lamprey in the Klamath also come in two forms, one that matures in the ocean and one "
            "that matures in the river, and they differ at several interacting genes.",
        ],
        "refs": [
            ("Thompson et al. 2020", D + "10.1126/science.aba9059"),
            ("Parker et al. 2019", D + "10.1111/mec.15136"),
            ("Hess et al. 2020", D + "10.1111/mec.15605"),
        ],
    },
    {
        "title": "Small and isolated populations",
        "body": [
            "Sandbars, and more recently dikes and tide gates, cut tidewater goby populations off from one another. "
            "In Humboldt Bay's fragmented sloughs we found strong genetic drift. Across northern California, "
            "populations stayed genetically stable through time, with no sign of the extinction and recolonization "
            "cycles seen farther south. Populations with low genetic diversity and a narrow range of ages were the "
            "ones most likely to disappear. A reference genome for the northern tidewater goby now supports the "
            "next round of work.",
        ],
        "refs": [
            ("McCraney et al. 2010", D + "10.1111/j.1365-294X.2010.04755.x"),
            ("Kinziger et al. 2015", D + "10.1111/mec.13424"),
            ("Hellmair and Kinziger 2014", D + "10.1371/journal.pone.0113139"),
            ("Jacobs et al. 2024", D + "10.1093/jhered/esae053"),
        ],
    },
    {
        "title": "Hidden diversity and reference genomes",
        "figure": {
            "src": "pit-sculpin-2008.jpg", "w": 1400, "h": 933,
            "alt": "Close view of a mottled brown sculpin in a photo tank, showing its broad head and fan-shaped pectoral fin.",
            "where": "",
            "caption": "Pit sculpin (*Cottus pitensis*) from Bear Creek, photographed on a collecting trip to the Pit River in August 2008.",
            "credit": "Kinziger Lab",
        },
        "body": [
            "Speckled dace in the Klamath and Trinity rivers look alike but belong to distinct genetic lineages. "
            "Rough sculpin above and below Pit River Falls, a barrier created by the Hat Creek fault, have diverged "
            "genetically. We contribute to reference genomes for California fishes, including speckled dace and "
            "tidewater goby. Earlier work described new species of sculpin and sorted out relationships among "
            "North American *Cottus*.",
        ],
        "refs": [
            ("Wiesenfeld et al. 2017", D + "10.1007/s10592-017-1027-6"),
            ("Kinziger et al. 2016", D + "10.1007/s10592-016-0859-9"),
            ("Baker et al. 2026", D + "10.1093/jhered/esag041"),
            ("Kinziger and Wood 2010", "http://www.mapress.com/zootaxa/2010/f/z02340p064f.pdf"),
        ],
    },
    {
        "title": "Hatcheries, stocks and hybrids",
        "body": [
            "Genetic pedigrees of Mad River Hatchery steelhead let us reconstruct things tags cannot, such as family "
            "sizes and the ages at which fish return. Related work documented hybridization between spring-run and "
            "fall-run Chinook at Trinity River Hatchery, mapped the population structure of Klamath basin Chinook, "
            "and found that coastal cutthroat trout and steelhead hybridize only to a limited degree.",
        ],
        "refs": [
            ("Kinziger, Fong and Garza 2022", D + "10.1002/nafm.10821"),
            ("Kinziger et al. 2008", D + "10.1577/M07-103.1"),
            ("Kinziger et al. 2013", D + "10.1080/00028487.2013.806351"),
            ("Rizza et al. 2023", D + "10.1093/jhered/esad022"),
        ],
    },
    {
        "title": "Where introduced fishes came from",
        "body": [
            "With the U.S. Forest Service Redwood Sciences Laboratory, we trace introduced fishes back to their "
            "sources and estimate how many founders it took. Sacramento pikeminnow in the Eel River, Klamath "
            "smallscale sucker in the Smith River and introduced speckled dace all tell the same story: a few fish "
            "from a nearby basin are enough to start a population.",
        ],
        "refs": [
            ("Pikeminnow, 2013", D + "10.1007/s10592-013-0516-5"),
            ("Smallscale sucker, 2021", D + "10.1111/jfb.14664"),
            ("Smallscale sucker, 2024", D + "10.1007/s10592-024-01651-5"),
            ("Speckled dace, 2011", D + "10.1002/ece3.8"),
            ("California roach, 2019", D + "10.1007/s10641-019-00870-x"),
        ],
    },
]

PARTNER_TEXT = [
    "We run eDNA and genetic samples for agencies, Tribes and conservation organizations. We can help design "
    "the sampling, supply field kits and training, run qPCR or metabarcoding, and help interpret the results.",
    "The lab has also supported wildlife studies on campus, from genetic mark and recapture of black bears to "
    "DNA barcoding for wildlife disease.",
]
PARTNERS = [
    "Hoopa Valley Tribe",
    "Yurok Tribe",
    "U.S. Fish and Wildlife Service",
    "NOAA Fisheries, Southwest Fisheries Science Center",
    "U.S. Forest Service, Redwood Sciences Laboratory",
    "California Department of Fish and Wildlife",
    "California Department of Transportation (Caltrans)",
    "California Cooperative Fish and Wildlife Research Unit",
    "Columbia River Inter-Tribal Fish Commission",
    "California Conservation Genomics Project",
    "CSU Council on Ocean Affairs, Science and Technology (COAST)",
    "California Trout (CalTrout)",
    "Stillwater Sciences",
    "FISHBIO",
]
PARTNER_NOTE = ""   # text confirmed November 18; the two Tribes added November 20
TOOLS = [
    "Quantitative PCR (QuantStudio 3) and droplet digital PCR",
    "eDNA metabarcoding with MiFish 12S primers",
    "SNP and microsatellite genotyping, Sanger sequencing",
    "Occupancy and population-genetic modeling in R",
]

# --------------------------------------------------------------------------
# PEOPLE
# --------------------------------------------------------------------------
PI = {
    "name": "Andrew P. Kinziger, Ph.D.",
    "photo": {"src": "andrew-kinziger.jpg", "w": 640, "h": 800, "alt": "Andrew Kinziger", "credit": "Kellie Jo Brown, Cal Poly Humboldt"},
    "roles": [
        "Professor and Chair, Department of Fisheries Biology",
        "Graduate Coordinator, Natural Resources M.S. program",
    ],
    "bio": [
        "Andrew has taught at Humboldt and mentored M.S. students since 2003. He uses genetic data to study the "
        "ecology, management and conservation of fishes, and much of his recent work is on "
        "environmental DNA. He co-edited the 2025 *Molecular Ecology Resources* special issue on Indigenous "
        "contributions to molecular ecology.",
        "Away from the lab he runs, hikes, surfs and plays basketball, and spends time outdoors in Humboldt "
        "County with his family.",
    ],
    "education": [
        ("Ph.D.", "Ecology, Evolution and Systematics, Saint Louis University, 2003"),
        ("M.S.", "Applied Ecology and Conservation Biology, Frostburg State University, 1998"),
        ("B.S.", "Environmental Science, St. Norbert College, 1996"),
    ],
    "courses": [
        "FISH 474 Conservation Genetics of Fish and Wildlife",
        "Earlier: Ichthyology; Techniques in Fisheries Biology",
    ],
}

PEOPLE_NOTE = ""

# status: "confirm" shows an amber chip in the draft; "" shows nothing
MEMBERS = [
    {"name": "Alec Bauer", "role": "Graduate student, Natural Resources M.S.", "project": "eDNA metabarcoding to monitor fish diversity in northern California", "status": ""},
    {"name": "Olivia Giovannetti", "role": "Graduate student, Natural Resources M.S.", "project": "eDNA metabarcoding of fishes in the Humboldt Wind Energy Area, with the COAST offshore surveys", "status": ""},
    {"name": "Laura Redfield", "role": "Graduate student, Natural Resources M.S.", "project": "Klamath River eDNA: informing sonar estimates of salmon abundance", "status": ""},
    {"name": "Heleen Mittry", "role": "Undergraduate researcher, Fisheries Biology", "project": "Klamath River eDNA: field sampling", "status": ""},
]
MEMBERS_NOTE = ""

# theme: "edna", "gen" or ""
ALUMNI = [
    {"year": 2026, "name": "Megan Boche", "thesis": "The effects of temperature on the persistence of environmental DNA in self-preserving filters", "url": DC + "2554", "theme": "edna", "after": ""},
    {"year": 2025, "name": "Johnathon M. Richardson", "thesis": "Using environmental DNA metabarcoding to investigate diversity and seasonal variation of fishes in Humboldt Bay, California", "url": DC + "2533", "theme": "edna", "after": "Post-Masters Research Associate, Waterpower Science and Ecology, Pacific Northwest National Laboratory"},
    {"year": 2024, "name": "Jacqueline M. Bridegum", "thesis": "Using environmental DNA methods for estimating juvenile Chinook salmon abundance", "url": DC + "735", "theme": "edna", "after": "Fish Biologist, U.S. Fish and Wildlife Service, Arcata"},
    {"year": 2024, "name": "Gavin B. Bandy", "thesis": "Evaluating the utility of tracers to characterize environmental DNA transport and inform detection of fishes in small streams", "url": DC + "727", "theme": "edna", "after": "Fisheries Biologist, Thomas Gast & Associates Environmental Consultants, Arcata"},
    {"year": 2023, "name": "Dylan J. Keel", "thesis": "Effects of depth, distance to shore, and water velocity on organismal and extra-organismal environmental DNA concentrations in a large river", "url": DC + "641", "theme": "edna", "after": "Ecologist, Resource Environmental Solutions"},
    {"year": 2021, "name": "Doyle J. Coyne", "thesis": "Comparison of standard and environmental DNA methods for estimating Chinook salmon smolt abundance in the Klamath River, California", "url": DC + "494", "theme": "edna", "after": "California Department of Fish and Wildlife"},
    {"year": 2020, "name": "Steven R. Fong", "thesis": "Spatial and temporal genetic structure of winter-run steelhead (*Oncorhynchus mykiss*) returning to the Mad River, California", "url": DC + "403", "theme": "gen", "after": "Ph.D. program, Michigan State University"},
    {"year": 2019, "name": "Chad M. Martel", "thesis": "Using environmental DNA and occupancy modeling to estimate rangewide metapopulation dynamics of the endangered tidewater goby *Eucyclogobius* spp.", "url": DC + "323", "theme": "edna", "after": "Hoopa Valley Tribal Fisheries"},
    {"year": 2018, "name": "Keith A. Parker", "thesis": "Evidence for the genetic basis and inheritance of ocean and river-maturing ecotypes of Pacific lamprey (*Entosphenus tridentatus*) in the Klamath River, California", "url": DC + "179", "theme": "gen", "after": "Senior Fisheries Biologist, Yurok Tribe; teaches at Cal Poly Humboldt"},
    {"year": 2018, "name": "Michael Sutter", "thesis": "Rangewide tidewater goby occupancy survey using environmental DNA", "url": DC + "125", "theme": "edna", "after": ""},
    {"year": 2016, "name": "Ryan W. Whitmore", "thesis": "Evaluation of parameter estimation and field application of transgenerational genetic mark-recapture", "url": DC + "5", "theme": "gen", "after": "Coho biologist, northern and central British Columbia"},
    {"year": 2016, "name": "Kevin D. Hinterman", "thesis": "Baseline monitoring and characterization of rocky intertidal fish communities in Northern California", "url": DC + "6", "theme": "", "after": "Animal Care Coordinator and Research Technician in Ichthyology, Moss Landing Marine Laboratories"},
    {"year": 2015, "name": "Molly C. Schmelzle", "thesis": "Using occupancy modeling to compare environmental DNA to traditional field methods for regional-scale monitoring of an endangered aquatic species", "url": DC + "1579", "theme": "edna", "after": ""},
    {"year": 2015, "name": "Conrad B. Newell", "thesis": "Spawning behavior induction, thermal tolerance and anisakid parasites of the federally endangered tidewater goby (*Eucyclogobius newberryi*)", "url": DC + "1575", "theme": "", "after": "Research biologist, Seattle Shellfish"},
    {"year": 2014, "name": "Jesse C. Wiesenfeld", "thesis": "Riverscape genetics identifies a cryptic lineage of speckled dace (*Rhinichthys osculus*) in the Klamath-Trinity Basin", "url": DC + "1580", "theme": "gen", "after": "Fisheries consulting, Sacramento"},
    {"year": 2011, "name": "James W. Hearsey", "thesis": "Run timing, fat content and maturity of spring- and fall-run Klamath River Chinook salmon (*Oncorhynchus tshawytscha*)", "url": DC + "1576", "theme": "gen", "after": "Fisheries Biologist, NOAA, Seattle"},
    {"year": 2011, "name": "Melissa R. Reneski", "thesis": "Temporal genetic analysis of steelhead (*Oncorhynchus mykiss*) reveals hatchery-induced drift in captivity", "url": DC + "1574", "theme": "gen", "after": "California Department of Fish and Wildlife"},
    {"year": 2011, "name": "Michael Hellmair", "thesis": "Life history variation and diet of the endangered tidewater goby, *Eucyclogobius newberryi*", "url": DC + "1577", "theme": "", "after": "Fish biologist, Lake Constance, Austria"},
    {"year": 2009, "name": "W. Tyler McCraney", "thesis": "Rampant drift in the endangered tidewater goby (*Eucyclogobius newberryi*): comparing genetic variation of naturally and artificially fragmented populations", "url": DC + "1578", "theme": "gen", "after": "Fisheries Geneticist, Northwest Indian Fisheries Commission; earlier Ph.D., UCLA, and postdoctoral researcher in the lab, 2020–2024"},
    {"year": 2007, "name": "David M. Malakauskas", "thesis": "Microsatellite evidence for short-term stability in a hybrid zone between spring-run and fall-run Chinook salmon", "url": DC + "1581", "theme": "gen", "after": ""},
    {"year": 2006, "name": "Damon H. Goodman", "thesis": "Evidence for high levels of gene flow among populations of a widely distributed anadromous lamprey *Entosphenus tridentatus* (Petromyzontidae)", "url": DC + "1877", "theme": "gen", "after": "Regional Director, California Trout"},
    {"year": 2006, "name": "Katie R. McGourty", "thesis": "Spawning time, fecundity, habitat utilization, and parasites of *Eucyclogobius newberryi* in Humboldt County, Big Lagoon, CA", "url": DC + "1582", "theme": "", "after": ""},
]
ALUMNI_NOTE = ""

# --------------------------------------------------------------------------
# PUBLICATIONS
# theme: edna | cons | genomics | invasion | syst | ecol | editorial
# --------------------------------------------------------------------------
THEMES = [
    ("edna", "eDNA", "edna"),
    ("cons", "Conservation genetics", "gen"),
    ("genomics", "Genomics and adaptation", "gen"),
    ("invasion", "Invasion genetics", "gen"),
    ("syst", "Systematics", "plain"),
    ("ecol", "Ecology and natural history", "plain"),
    ("editorial", "Editorials", "plain"),
]

PUBLICATIONS = [
    {"a": "Henry K Baker, Merly Escalona, Andrew P Kinziger, Jeff Rodzen, Steve Parmenter, Mohan P A Marimuthu, Oanh Nguyen, Noravit Chumchim, Eric Beraut, Samuel Sacco, William Seligmann, Colin W Fairbairn, Robert D Cooper, Courtney Miller, Erin Toffelmier, J Carlos Garza, H Bradley Shaffer, Jonathan B Shurin, Diana J Rennison",
     "y": 2026, "t": "A genome assembly of the speckled dace, *Rhinichthys osculus*", "j": "Journal of Heredity", "d": "esag041", "doi": "10.1093/jhered/esag041", "theme": "genomics"},
    {"a": "Ramos, S. C., Kinziger, A.P., A. Alexander",
     "y": 2025, "t": "Hīkina te mānuka: Advancing Indigenous Leadership in Molecular Ecology", "j": "Molecular Ecology Resources", "d": "25(2):e14049", "doi": "10.1111/1755-0998.14049", "theme": "editorial"},
    {"a": "Kinziger, A. P., Fong, S. R., Nakamoto, R. J., White, J. L., & Harvey, B. C.",
     "y": 2024, "t": "Contemporary evolution of neutral genetic structure in introduced Klamath smallscale suckers (*Catostomus rimiculus*) recapitulates native patterns", "j": "Conservation Genetics", "d": "", "doi": "10.1007/s10592-024-01651-5", "theme": "invasion",
     "extra": [("Read free", "https://rdcu.be/dXj7S")]},
    {"a": "David K Jacobs, Andrew Kinziger, Mira Abrecht, W Tyler McCraney, Benjamin A Hà, Brenton T Spies, Elizabeth Heath-Heckman, Mohan P A Marimuthu, Oanh Nguyen, Colin W Fairbairn, William E Seligmann, Merly Escalona, Courtney Miller, H Bradley Shaffer",
     "y": 2024, "t": "Reference genome for the endangered, genetically subdivided, northern tidewater goby, *Eucyclogobius newberryi*", "j": "Journal of Heredity", "d": "esae053", "doi": "10.1093/jhered/esae053", "theme": "genomics"},
    {"a": "Shaffer, J. T., Kinziger, A. P., Bjorkstedt, E. P., & Buchheister, A.",
     "y": 2024, "t": "Comparison of environmental DNA and underwater visual count surveys for detecting juvenile Coho Salmon in small rivers", "j": "North American Journal of Fisheries Management", "d": "", "doi": "10.1002/nafm.10993", "theme": "edna"},
    {"a": "Schuiteman, M., Dos Santos, A. R., Domínguez-Granda, L. E., Kinziger, A., & Marin Jarrin, J. R.",
     "y": 2024, "t": "Age and growth of larval Pacific flagfin mojarra (*Eucinostomus currani*) in coastal Ecuador based on otolith analysis", "j": "Ciencias Marinas", "d": "50", "doi": "10.7773/cm.y2024.3448", "theme": "ecol"},
    {"a": "Rizza, S.F., M.A. Wilzbach, A.P. Kinziger, E.C. Anderson, and J.C. Garza",
     "y": 2023, "t": "Limited, asymmetric hybridization between coastal cutthroat trout and steelhead in a Northern California river", "j": "Journal of Heredity", "d": "114:219–230", "doi": "10.1093/jhered/esad022", "theme": "cons"},
    {"a": "Burris, W.M., A.P. Kinziger, J.M. Black, and R.N. Brown",
     "y": 2022, "t": "*Knemidokoptes* mites and their effects on the gripping position of Steller's Jay (*Cyanocitta stelleri*) feet", "j": "Journal of Wildlife Diseases", "d": "58(4):859–868", "doi": "10.7589/JWD-D-22-00016", "theme": "ecol"},
    {"a": "Kinziger, A.P., S.R. Fong, J.C. Garza",
     "y": 2022, "t": "Pedigree analysis of an integrated hatchery steelhead program from the Mad River, California provides insight into life-history patterns and informs management", "j": "North American Journal of Fisheries Management", "d": "42:1285–1295", "doi": "10.1002/nafm.10821", "theme": "cons"},
    {"a": "Martel C, Sutter M, Dorazio R, Kinziger AP",
     "y": 2021, "t": "Using environmental DNA and occupancy modelling to estimate rangewide metapopulation dynamics", "j": "Molecular Ecology", "d": "30:3340–3354", "doi": "10.1111/mec.15693", "theme": "edna",
     "press": [("Caltrans: eDNA Speeds Up Road Maintenance, p. 11", "https://dot.ca.gov/-/media/dot-media/programs/research-innovation-system-information/documents/drisi-caltrans-solution-lab-v33-a11y.pdf")]},
    {"a": "Rodríguez-Ezpeleta, N., L. Zinger, A.P. Kinziger, H.M. Bik, A. Bonin, E. Coissac, B.C Emerson, C. Martins Lopes, T.A. Pelletier, P Taberlet, S. Narum",
     "y": 2021, "t": "Biodiversity monitoring using environmental DNA", "j": "Molecular Ecology Resources", "d": "21:1405–1409", "doi": "10.1111/1755-0998.13399", "theme": "edna"},
    {"a": "Kinziger, A.P., White, J.L., Nakamoto, R.J., and B.C. Harvey",
     "y": 2021, "t": "Recent, small beginnings: genetic analysis suggests *Catostomus rimiculus* (Klamath smallscale sucker) in the Smith River, California, are introduced", "j": "Journal of Fish Biology", "d": "98:1321–1328", "doi": "10.1111/jfb.14664", "theme": "invasion"},
    {"a": "Marden, E., R.J. Abbott, F. Austerlitz, D. Ortiz‐Barrientos, R. S. Baucom, P. Bongaerts … A.P. Kinziger … L.H. Rieseberg",
     "y": 2020, "t": "Sharing and reporting benefits from biodiversity research", "j": "Molecular Ecology", "d": "30:1103–1107", "doi": "10.1111/mec.15702", "theme": "editorial"},
    {"a": "Thompson, N.F., E.C. Anderson, A.J. Clemento, M.A Campbell, D.E. Pearse, J.W. Hearsey, A.P. Kinziger, and J.C. Garza",
     "y": 2020, "t": "A complex phenotype in salmon controlled by a simple change in migratory timing", "j": "Science", "d": "370(6516):609–613", "doi": "10.1126/science.aba9059", "theme": "genomics",
     "press": [
         ("Science Perspective", "https://science.sciencemag.org/content/370/6516/526"),
         ("National Geographic", "https://www.nationalgeographic.com/environment/2020/11/dam-removal-project-genetic-discovery-could-be-good-news-for-key-salmon-species/"),
         ("UC Santa Cruz", "https://www.eurekalert.org/news-releases/482684"),
         ("Humboldt Now", "http://now.humboldt.edu/news/a-tiny-difference-in-genetics-is-good-news-for-salmon-conservation/"),
         ("Cell", "https://www.sciencedirect.com/science/article/pii/S0092867420317591"),
     ]},
    {"a": "Hess, J., J. Smith, N. Timoshevskaya, C. Baker, C. Caudill, D. Graves, M. Keefer, A. Kinziger, M. Moser, L. Porter, G. Silver, S. Whitlock, and S. Narum",
     "y": 2020, "t": "Genomic islands of divergence infer a phenotypic landscape in Pacific lamprey", "j": "Molecular Ecology", "d": "29:3841–3856", "doi": "10.1111/mec.15605", "theme": "genomics"},
    {"a": "Parker KA, Hess JE, Narum SR, Kinziger AP",
     "y": 2019, "t": "Evidence for the genetic basis and epistatic interactions underlying ocean‐ and river‐maturing ecotypes of Pacific lamprey (*Entosphenus tridentatus*) returning to the Klamath River, California", "j": "Molecular Ecology", "d": "28:3171–3185", "doi": "10.1111/mec.15136", "theme": "genomics"},
    {"a": "Kinziger, A.P., R.J. Nakamoto, A. Aguilar, B.C. Harvey",
     "y": 2019, "t": "California roach (*Hesperoleucus symmetricus*) in the Eel River of northwestern California: native or introduced?", "j": "Environmental Biology of Fishes", "d": "102:771–781", "doi": "10.1007/s10641-019-00870-x", "theme": "invasion"},
    {"a": "Sutter, M., and A.P. Kinziger",
     "y": 2019, "t": "Rangewide tidewater goby occupancy survey using environmental DNA", "j": "Conservation Genetics", "d": "20:597–613", "doi": "10.1007/s10592-019-01161-9", "theme": "edna"},
    {"a": "Wiesenfeld, J.C., D.H. Goodman, and A.P. Kinziger",
     "y": 2017, "t": "Riverscape genetics identifies speckled dace (*Rhinichthys osculus*) cryptic diversity in the Klamath-Trinity Basin", "j": "Conservation Genetics", "d": "19:111–127", "doi": "10.1007/s10592-017-1027-6", "theme": "cons"},
    {"a": "Baumsteiger, J., A.P. Kinziger, A. Aguilar",
     "y": 2016, "t": "Novel concordance between geographic, environmental, and genetic structure in the ecological generalist prickly sculpin (*Cottus asper*) in California", "j": "Journal of Heredity", "d": "107:504–517", "doi": "10.1093/jhered/esw045", "theme": "cons"},
    {"a": "Olsen, J.B., A.P. Kinziger, J.K. Wenburg, C.J. Lewis, C.T. Phillips, K.G. Ostrand",
     "y": 2016, "t": "Genetic diversity and divergence in the fountain darter (*Etheostoma fonticola*): implications for conservation of an endangered species", "j": "Conservation Genetics", "d": "17:1393–1404", "doi": "10.1007/s10592-016-0869-7", "theme": "cons"},
    {"a": "Kinziger, A.P., M. Hellmair, S.R. Fong, D.H. Goodman, H. Kelsey",
     "y": 2016, "t": "Evolution of rough sculpin (*Cottus asperrimus*) genetic divergence and late Quaternary displacement on the Hat Creek fault, California, USA", "j": "Conservation Genetics", "d": "17:1257–1267", "doi": "10.1007/s10592-016-0859-9", "theme": "cons"},
    {"a": "Schmelzle, M.C., and A.P. Kinziger",
     "y": 2016, "t": "Using occupancy modeling to compare environmental DNA to traditional field methods for regional-scale monitoring of an endangered aquatic species", "j": "Molecular Ecology Resources", "d": "16:895–908", "doi": "10.1111/1755-0998.12501", "theme": "edna"},
    {"a": "Kinziger, A.P., M. Hellmair, W. T. McCraney, D.K. Jacobs, G. Goldsmith",
     "y": 2015, "t": "Temporal genetic analysis of the endangered tidewater goby: extinction–colonization dynamics or drift in isolation?", "j": "Molecular Ecology", "d": "24:5544–5560", "doi": "10.1111/mec.13424", "theme": "cons"},
    {"a": "Wallace, M., E.W. Ojerholm, A.J. Scheiff, and A.P. Kinziger",
     "y": 2015, "t": "First record of striped mullet (*Mugil cephalus*) in Humboldt Bay, California", "j": "California Fish and Game", "d": "101(4):286–288", "url": "https://nrm.dfg.ca.gov/FileHandler.ashx?DocumentID=113248&inline", "theme": "ecol"},
    {"a": "Hellmair, M., and A.P. Kinziger",
     "y": 2014, "t": "Increased extinction potential of insular fish populations with reduced life history variation and low genetic diversity", "j": "PLoS ONE", "d": "9(11):e113139", "doi": "10.1371/journal.pone.0113139", "theme": "cons"},
    {"a": "Baumsteiger, J., A.P. Kinziger, S.B. Reid, A. Aguilar",
     "y": 2014, "t": "Complex phylogeography and historical hybridization between sister taxa of freshwater sculpin (*Cottus*)", "j": "Molecular Ecology", "d": "23:2602–2618", "doi": "10.1111/mec.12758", "theme": "syst"},
    {"a": "Hearsey, J.W., and A.P. Kinziger",
     "y": 2014, "t": "Diversity in sympatric Chinook salmon runs – timing, relative fat content and maturation", "j": "Environmental Biology of Fishes", "d": "98:413–423", "doi": "10.1007/s10641-014-0272-5", "theme": "cons"},
    {"a": "Kinziger, A. P., R.J. Nakamoto, and B.C. Harvey",
     "y": 2013, "t": "Local-scale invasion pathways and small founder numbers in introduced Sacramento pikeminnow (*Ptychocheilus grandis*)", "j": "Conservation Genetics", "d": "15:1–9", "doi": "10.1007/s10592-013-0516-5", "theme": "invasion"},
    {"a": "Kinziger, A. P., M. Hellmair, D.G. Hankin, and J.C. Garza",
     "y": 2013, "t": "Contemporary population structure in Klamath River basin Chinook salmon revealed by analysis of microsatellite genetic data", "j": "Transactions of the American Fisheries Society", "d": "142:1347–1357", "doi": "10.1080/00028487.2013.806351", "theme": "cons"},
    {"a": "Baumsteiger, J., A.P. Kinziger, and A. Aguilar",
     "y": 2012, "t": "Life history and biogeographic diversification of an endemic western North American freshwater fish clade using a comparative species tree approach", "j": "Molecular Phylogenetics and Evolution", "d": "65:940–952", "url": "https://www.sciencedirect.com/science/article/pii/S1055790312003247", "theme": "syst"},
    {"a": "Kinziger, A. P., R.J. Nakamoto, E.C. Anderson, and B.C. Harvey",
     "y": 2011, "t": "Small founding number and low genetic diversity in an introduced species exhibiting limited invasion success (speckled dace, *Rhinichthys osculus*)", "j": "Ecology and Evolution", "d": "1:73–84", "doi": "10.1002/ece3.8", "theme": "invasion"},
    {"a": "Hellmair, M., G. Goldsmith, and A.P. Kinziger",
     "y": 2011, "t": "Preying on invasives: the exotic New Zealand mudsnail in the diet of the endangered tidewater goby", "j": "Biological Invasions", "d": "13:2197–2201", "doi": "10.1007/s10530-011-0054-3", "theme": "ecol"},
    {"a": "McCraney, W. T., G. Goldsmith, D.K. Jacobs, and A.P. Kinziger",
     "y": 2010, "t": "Rampant drift in artificially fragmented populations of the endangered tidewater goby (*Eucyclogobius newberryi*)", "j": "Molecular Ecology", "d": "19:3315–3327", "doi": "10.1111/j.1365-294X.2010.04755.x", "theme": "cons"},
    {"a": "Kinziger, A.P., and R.M. Wood",
     "y": 2010, "t": "*Cottus immaculatus*, a new species of sculpin (Cottidae) from the Ozark Highlands of Arkansas and Missouri, USA", "j": "Zootaxa", "d": "2340:50–64", "url": "http://www.mapress.com/zootaxa/2010/f/z02340p064f.pdf", "theme": "syst"},
    {"a": "Goodman, D.H., A.P. Kinziger, S.B. Reid, and M.F. Docker",
     "y": 2009, "t": "Morphological diagnosis of *Entosphenus* and *Lampetra* ammocoetes (Petromyzontidae) in Washington, Oregon, and California", "j": "American Fisheries Society Symposium", "d": "72:223–232", "theme": "syst"},
    {"a": "Kinziger, A.P., E. J. Loudenslager, D.G. Hankin, J.C. Garza and E.C. Anderson",
     "y": 2008, "t": "Hybridization between spring-run and fall-run Chinook salmon returning to the Trinity River Hatchery", "j": "North American Journal of Fisheries Management", "d": "28:1426–1438", "doi": "10.1577/M07-103.1", "theme": "cons"},
    {"a": "McGourty, K.M., A.P. Kinziger, and G. Goldsmith",
     "y": 2008, "t": "Spawning time, fecundity, habitat utilization, and parasites of a northern California population of tidewater goby, *Eucyclogobius newberryi*", "j": "California Fish and Game", "d": "94(1):18–32", "theme": "ecol"},
    {"a": "Goodman, D.H., S.B. Reid, M.F. Docker, A.P. Kinziger, and G.R. Haas",
     "y": 2008, "t": "Evidence for high levels of gene flow among populations of a widely distributed anadromous lamprey *Entosphenus tridentatus* (Petromyzontidae)", "j": "Journal of Fish Biology", "d": "72:400–417", "doi": "10.1111/j.1095-8649.2007.01731.x", "theme": "cons"},
    {"a": "Kinziger, A.P., D.H. Goodman and R.S. Studebaker",
     "y": 2007, "t": "Mitochondrial DNA variation in the Ozark Highland members of the *Cottus carolinae* complex (Scorpaeniformes: Cottidae)", "j": "Transactions of the American Fisheries Society", "d": "136:1742–1749", "doi": "10.1577/T06-025.1", "theme": "syst"},
    {"a": "McGourty, K.M., A.P. Kinziger, G.H. Hendrickson, G. Goldsmith and C. Graça",
     "y": 2007, "t": "*Kabatana newberryi* n. sp., a microsporidium infecting the musculature of the endangered tidewater goby (*Eucyclogobius newberryi*)", "j": "Journal of Parasitology", "d": "93:655–660", "theme": "ecol"},
    {"a": "Kinziger, A.P., R.M. Wood and D.A. Neely",
     "y": 2005, "t": "Molecular systematics and classification of *Cottus* and the Baikalian cottoids (Scorpaeniformes)", "j": "Copeia", "d": "2005:303–311", "doi": "10.1643/CI-03-290R1", "theme": "syst"},
    {"a": "Kinziger, A.P.",
     "y": 2003, "t": "Evidence supporting two new forms and one previously described race within the *Cottus carolinae* species-complex from the Ozark Highlands", "j": "American Midland Naturalist", "d": "149:418–424", "doi": "10.1674/0003-0031(2003)149[0418:ESTNFA]2.0.CO;2", "theme": "syst"},
    {"a": "Kinziger, A.P. and R.M. Wood",
     "y": 2003, "t": "Molecular systematics of the polytypic species *Cottus hypselurus* (Teleostei: Cottidae)", "j": "Copeia", "d": "2003:624–627", "doi": "10.1643/CI-02-240R", "theme": "syst"},
    {"a": "Cochran, P.A., J.Y. Hodgson, and A.P. Kinziger",
     "y": 2003, "t": "Change in the energy density of the sea lamprey (*Petromyzon marinus*) during its parasitic phase: implications for modeling food consumption and growth", "j": "Journal of Great Lakes Research", "d": "29 (Supplement 1):297–306", "url": "https://www.sciencedirect.com/science/article/pii/S038013300370495X", "theme": "ecol"},
    {"a": "Kinziger, A.P., P.A. Cochran, and J.A. Cochran",
     "y": 2002, "t": "Additional cases of predation on horsehair worms (Phylum Nematomorpha), with a first record for Missouri", "j": "MO. Acad. Sci. Bull.", "d": "36:11–13", "theme": "ecol"},
    {"a": "Kinziger, A.P. and R.L. Raesly",
     "y": 2001, "t": "A narrow hybrid zone between two species of *Cottus* in Wills Creek, Potomac drainage", "j": "Journal of Heredity", "d": "92:309–314", "url": "https://academic.oup.com/jhered/article-abstract/92/4/309/2187151", "theme": "syst"},
    {"a": "Kinziger, A.P., R.M. Wood, and S.A. Welsh",
     "y": 2001, "t": "Systematics of *Etheostoma tippecanoe* and *Etheostoma denoncourti* (Perciformes: Percidae)", "j": "Copeia", "d": "2001:235–239", "url": "https://www.jstor.org/stable/1448116", "theme": "syst"},
    {"a": "Kinziger, A.P., R.L. Raesly, and D.A. Neely",
     "y": 2000, "t": "New species of *Cottus* (Teleostei: Cottidae) from the Middle Atlantic Eastern United States", "j": "Copeia", "d": "2000:1007–1018", "doi": "10.1643/0045-8511(2000)000[1007:NSOCTC]2.0.CO;2", "theme": "syst"},
    {"a": "Cochran, P.A., W.D. Swink, and A.P. Kinziger",
     "y": 1999, "t": "Testing and extension of a sea lamprey feeding model", "j": "Transactions of the American Fisheries Society", "d": "128:403–413", "doi": "10.1577/1548-8659(1999)128<0403:TAEOAS>2.0.CO;2", "theme": "ecol"},
    {"a": "Cochran, P.A., A.P. Kinziger, and W.J. Poly",
     "y": 1999, "t": "Predation on horsehair worms (Phylum Nematomorpha)", "j": "Journal of Freshwater Ecology", "d": "14:211–218", "theme": "ecol"},
    {"a": "Kinziger, A.P.",
     "y": 1998, "t": "Comparison of weight-length regressions for slimy sculpin (*Cottus cognatus*) and mottled sculpin (*C. bairdi*) from the West Twin river drainage, Wisconsin", "j": "BIOS", "d": "69:1–6", "theme": "ecol"},
    {"a": "Cochran, P.A. and A.P. Kinziger",
     "y": 1997, "t": "*Hexagenia bilineata* (Ephemeroptera: Ephemeridae) persists at low levels of abundance in the lower Fox river, Wisconsin", "j": "Great Lakes Entomologist", "d": "30:89–92", "theme": "ecol"},
    {"a": "Kinziger, A.P.",
     "y": 1997, "t": "Winter roost habitat and diet of short-eared owls (*Asio flammeus*) in Door County, Wisconsin", "j": "Passenger Pigeon", "d": "59:45–52", "theme": "ecol"},
]

PUBS_NOTE = ""   # list confirmed November 18

# --------------------------------------------------------------------------
# JOIN
# --------------------------------------------------------------------------
JOIN_INTRO = (
    "We take M.S. students through the Natural Resources graduate program at Cal Poly Humboldt, in the Fisheries "
    "concentration. The lab usually has about three graduate students at a time, so space is limited."
)
JOIN_PHOTO = {
    "src": "little-jones-creek-2014.jpg", "w": 1200, "h": 900,
    "alt": "A researcher holds a tall survey rod beside a waterfall that drops into a pool in a forested ravine.",
    "where": "Little Jones Creek, Smith River basin",
    "caption": "Measuring a waterfall during a survey of barriers to fish movement, October 2014.",
    "credit": "Kinziger Lab",
}
JOIN_STEPS = [
    ("Get in touch",
     "If your research interests match the lab's work in environmental DNA and conservation genetics, let Andrew "
     "know. It helps to send a CV or résumé, a writing sample, and a short description of your research experience, "
     "what you want to study and your long-term goals."),
    ("Visit or call",
     "If your interests fit and the lab has space, Andrew may invite you to visit campus or set up a call."),
    ("Apply through Cal State Apply",
     "The application asks for transcripts, three references, a statement of purpose and a résumé. "
     "[Application steps for the Natural Resources M.S.](https://www.humboldt.edu/cnrs/graduate-programs/natural-resources)"),
]
DEADLINES = [
    ("Fall admission", "Applications open October 1 and close February 1"),
    ("Spring admission", "Applications open August 1 and close September 30"),
]
DEADLINES_SRC = ("Graduate application deadlines at Cal Poly Humboldt", "https://www.humboldt.edu/admission-aid/how-to-apply/graduate")
FUNDING = (
    "Most graduate students in the lab receive funding that covers a small salary, full or partial tuition, "
    "research expenses and travel to conferences. Funding is not guaranteed, and it is not a requirement for "
    "admission. Support usually comes from the research grant or contract behind the thesis project, supplemented "
    "by teaching or graduate assistantships and scholarships. We encourage students to apply for Fisheries Biology "
    "scholarships and for California State University awards such as COAST and CSUPERB."
)
JOIN_NOTE = ""
UNDERGRAD = (
    "Cal Poly Humboldt undergraduates work in the lab on eDNA projects: filtering water, extracting DNA and "
    "setting up qPCR. FISH 474, Conservation Genetics of Fish and Wildlife, includes hands-on eDNA labs. If you "
    "want research experience, email Andrew or stop by Wildlife and Fisheries 214."
)

# --------------------------------------------------------------------------
# CONTACT
# --------------------------------------------------------------------------
CONTACT = {
    "name": "Dr. Andrew Kinziger",
    "lines": [
        "Department of Fisheries Biology",
        "Cal Poly Humboldt",
        "1 Harpst Street, Arcata, CA 95521",
    ],
    "rooms": [("Office", "Wildlife and Fisheries 210"), ("Lab", "Wildlife and Fisheries 214")],
    "phone": "(707) 826-3944",
    "email": "andrew.kinziger@humboldt.edu",
    "links": [
        ("Department of Fisheries Biology", "https://www.humboldt.edu/fisheries-biology"),
        ("Natural Resources M.S. program", "https://www.humboldt.edu/cnrs/graduate-programs/natural-resources"),
        ("Faculty profile", "https://www.humboldt.edu/fisheries-biology/andrew-kinziger"),
    ],
}
UPDATED = "November 2026"

# --------------------------------------------------------------------------
# VISIT COUNTER
# --------------------------------------------------------------------------
# GoatCounter account name; the dashboard is at https://<name>.goatcounter.com.
# Set this to "" to stop counting visits.
GOATCOUNTER = "kinzigerlab"
