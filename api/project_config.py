from .project_catagories.blogs import BLOGS
from .project_catagories.offers import OFFERS_PROJECTS
from .project_catagories.quizzes import QUIZZES_PROJECTS
from .project_catagories.social_media import SOCIAL_MEDIA
from .project_catagories.surveys import SURVEYS_PROJECTS
from .project_catagories.emails import EMAILS
from .project_catagories.ads import ADS
from .project_catagories.ecommerce import ECOMMERCE
from .project_catagories.frameworks import FRAMEWORK
from .project_catagories.marketing import MARKETING
from .project_catagories.seo import SEO
from .project_catagories.video import VIDEO
from .project_catagories.website import WEBSITE

PROJECT_CATEGORIES = {
    # 'categories' : 'projects'
    "quizzes": QUIZZES_PROJECTS,
    "offers": OFFERS_PROJECTS,
    "surveys": SURVEYS_PROJECTS,
    "blogs": BLOGS,
    "emails": EMAILS,
    "ads": ADS,
    "ecommerce": ECOMMERCE,
    "framework": FRAMEWORK,
    "marketing": MARKETING,
    "seo": SEO,
    "social_media": SOCIAL_MEDIA,
    "website": WEBSITE,
    "video": VIDEO
}
