import frontmatter
import inflection
import os
import typer

from datetime import date, datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from pathlib import Path
from pydantic import BaseModel, Field, ValidationError
from slugify import slugify
from typing import List, Optional
import pytz

CONFERENCE_TZ = pytz.timezone("America/Los_Angeles")


class FrontmatterModel(BaseModel):
    """
    Our base class for our default "Frontmatter" fields.
    """

    date: Optional[datetime]
    layout: str
    permalink: Optional[str]
    published: bool = True
    redirect_from: Optional[List[str]]
    redirect_to: Optional[str]  # via the jekyll-redirect-from plugin
    sitemap: Optional[bool]
    title: str

    class Config:
        extra = "allow"


class Job(FrontmatterModel):
    hidden: bool = False
    layout: str = "base"
    name: str
    title: Optional[str]
    website: str
    website_text: str = "Apply here"


class Organizer(FrontmatterModel):
    github: Optional[str]
    hidden: bool = False
    layout: str = "base"
    name: str
    photo_url: Optional[str]
    slug: Optional[str]
    title: Optional[str]
    twitter: Optional[str]
    website: Optional[str]


class Page(FrontmatterModel):
    description: Optional[str]
    heading: Optional[str]
    hero_text_align: Optional[str]  # homepage related
    hero_theme: Optional[str]  # homepage related
    layout: Optional[str]
    testimonial_img: Optional[str]  # homepage related
    testimonial_img_mobile: Optional[str]  # homepage related
    title: Optional[str]


class Post(FrontmatterModel):
    author: Optional[str] = None
    category: Optional[str] = "General"  # TODO: build a list of these
    categories: Optional[List[str]]
    date: datetime  # YYYY-MM-DD HH:MM:SS +/-TTTT
    image: Optional[str] = None
    layout: Optional[str] = "post"
    slug: Optional[str] = None
    tags: Optional[List[str]]


class Presenter(FrontmatterModel):
    company: Optional[str]
    github: Optional[str]
    hidden: bool = False
    layout: str = "speaker-template"
    name: str
    override_schedule_title: Optional[str] = None
    photo_url: Optional[str]
    role: Optional[str]
    title: Optional[str]
    twitter: Optional[str]
    website: Optional[str]
    website_text: str = "Apply here"


class Schedule(FrontmatterModel):
    abstract: Optional[str] = None
    accepted: bool = False
    category: Optional[str] = "talk"
    difficulty: Optional[str] = "All"
    image: Optional[str]
    layout: Optional[str] = "session-details"  # TODO: validate against _layouts/*.html
    presenter_slugs: Optional[List[str]] = None
    presenters: List[dict] = None  # TODO: break this into a sub-type
    published: bool = False
    room: Optional[str]
    schedule: Optional[str]
    schedule_layout: Optional[str] = Field(
        alias="schedule-layout"
    )  # TODO: Validate for breaks, lunch, etc
    show_video_urls: Optional[bool]
    slides_url: Optional[str]
    summary: Optional[str]
    end_date: Optional[datetime] = None
    tags: Optional[List[str]] = None
    talk_slot: Optional[str] = "full"
    track: Optional[str] = None
    video_url: Optional[str]


POST_TYPES = [
    {"path": "_jobs", "class_name": Job},
    {"path": "_organizers", "class_name": Organizer},
    {"path": "_pages", "class_name": Page},
    {"path": "_posts", "class_name": Post},
    {"path": "_presenters", "class_name": Presenter},
    {"path": "_schedule/talks", "class_name": Schedule},
]

app = typer.Typer()


@app.command()
def fmt():
    for post_type in POST_TYPES:
        filenames = sorted(list(Path(post_type["path"]).glob("**/*")))

        for filename in filenames:
            try:
                post = frontmatter.loads(filename.read_text())
                data = post_type["class_name"](**post.metadata)
                post.metadata.update(data.dict(exclude_unset=True))
                filename.write_text(frontmatter.dumps(post) + os.linesep)
            except ValidationError as e:
                typer.secho(f"{filename}", fg="red")
                typer.echo(e.json())
            except Exception as e:
                typer.secho(f"{filename}::{e}", fg="red")


@app.command()
def validate():
    for post_type in POST_TYPES:
        filenames = sorted(list(Path(post_type["path"]).glob("**/*")))

        for filename in filenames:
            try:
                data = frontmatter.loads(filename.read_text())
                post_type["class_name"](**data.metadata)
            except ValidationError as e:
                typer.secho(f"{filename}", fg="red")
                typer.echo(e.json())
            except Exception as e:
                typer.secho(f"{filename}::{e}", fg="red")


@app.command()
def generate_lactation_room(
    event_date: datetime,
    link: str = "",  # TODO update this to /news/lactation-room/ after we make the blog post
    room_name: str = "Santa Fe 3",
    start_time: str = "8:00",
    end_time: str = "17:30",
):
    category = "talks"
    if event_date.weekday() == 6:
        category = "tutorials"
    elif event_date.weekday() in {3, 4}:
        category = "sprints"

    parsed_start = parse(start_time).time()
    parsed_end = parse(end_time).time()
    if isinstance(event_date, date) and not isinstance(event_date, datetime):
        start = CONFERENCE_TZ.localize(datetime.combine(event_date, parsed_start))
        end = CONFERENCE_TZ.localize(datetime.combine(event_date, parsed_end))
    else:
        start = CONFERENCE_TZ.localize(
            datetime.combine(event_date.date(), parsed_start)
        )
        end = CONFERENCE_TZ.localize(datetime.combine(event_date.date(), parsed_end))
    post = frontmatter.loads(room_name)
    sched = Schedule(
        accepted=True,
        layout="session-details",
        category=category,
        date=start,
        end_date=end,
        room=room_name,
        schedule_layout="full",
        sitemap=False,
        title="Lactation Room",
        permalink=None,
        link=link or None,
    )
    post.metadata.update(sched.dict(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}"
        f"-{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-lactation-room.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_quiet_room(
    event_date: datetime,
    room_name: str = "Private Dining Room",
    start_time: str = "8:00",
    end_time: str = "18:00",
):
    category = "talks"
    if event_date.weekday() == 6:
        category = "tutorials"
    elif event_date.weekday() in {3, 4}:
        category = "sprints"

    parsed_start = parse(start_time).time()
    parsed_end = parse(end_time).time()
    if isinstance(event_date, date) and not isinstance(event_date, datetime):
        start = CONFERENCE_TZ.localize(datetime.combine(event_date, parsed_start))
        end = CONFERENCE_TZ.localize(datetime.combine(event_date, parsed_end))
    else:
        start = CONFERENCE_TZ.localize(
            datetime.combine(event_date.date(), parsed_start)
        )
        end = CONFERENCE_TZ.localize(datetime.combine(event_date.date(), parsed_end))
    post = frontmatter.loads(room_name)
    sched = Schedule(
        accepted=True,
        layout="session-details",
        category=category,
        date=start,
        end_date=end,
        room=room_name,
        schedule_layout="full",
        sitemap=False,
        title="Quiet Room",
        permalink=None,
        link=None,
    )
    post.metadata.update(sched.dict(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-quiet-room.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_registration_desk(
    event_date: datetime,
    location: str = "In front of Salon A",
    start_time: str = "8:00",
    end_time: str = "18:00",
):
    category = "talks"
    if event_date.weekday() == 6:
        category = "tutorials"
    elif event_date.weekday() in {3, 4}:
        raise ValueError("We don't have a registration desk on sprint days")

    parsed_start = parse(start_time).time()
    parsed_end = parse(end_time).time()
    if isinstance(event_date, date) and not isinstance(event_date, datetime):
        start = CONFERENCE_TZ.localize(datetime.combine(event_date, parsed_start))
        end = CONFERENCE_TZ.localize(datetime.combine(event_date, parsed_end))
    else:
        start = CONFERENCE_TZ.localize(
            datetime.combine(event_date.date(), parsed_start)
        )
        end = CONFERENCE_TZ.localize(datetime.combine(event_date.date(), parsed_end))
    post = frontmatter.loads(location)
    sched = Schedule(
        accepted=True,
        layout="session-details",
        category=category,
        date=start,
        end_date=end,
        room=location,
        schedule_layout="full",
        sitemap=False,
        title="Registration",
        permalink=None,
        link=None,
    )
    post.metadata.update(sched.dict(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-registration.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_breakfast(start_time: datetime, location: str = "Rio Vista Pavilion"):
    category = "talks"
    if start_time.weekday() == 6:
        category = "tutorials"
    elif start_time.weekday() in {3, 4}:
        category = "sprints"
    start_time = CONFERENCE_TZ.localize(start_time)
    end_time = start_time + relativedelta(hours=1)
    post = frontmatter.loads(location)
    sched = Schedule(
        accepted=True,
        layout="session-details",
        category=category,
        date=start_time,
        end_date=end_time,
        room=location,
        schedule_layout="full",
        sitemap=False,
        title="Continental Breakfast",
        permalink=None,
        link="/catering-menus/",
    )
    post.metadata.update(sched.dict(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_break(
    start_time: datetime,
    duration_minutes: int = 30,
    location: str = "Rio Vista Pavilion",
):
    category = "talks"
    if start_time.weekday() == 6:
        category = "tutorials"
    elif start_time.weekday() in {3, 4}:
        raise ValueError("We don't have published breaks on sprint days")
    start_time = CONFERENCE_TZ.localize(start_time)
    end_time = start_time + relativedelta(minutes=duration_minutes)
    post = frontmatter.loads(location)
    sched = Schedule(
        accepted=True,
        layout="session-details",
        category=category,
        date=start_time,
        end_date=end_time,
        room=location,
        schedule_layout="full",
        sitemap=False,
        title="Break",
        permalink=None,
        link=None,
    )
    post.metadata.update(sched.dict(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def generate_lightning_talks(
    start_time: datetime,
    duration_minutes: int = 50,
    location: str = "Salon A-E",
    track: int = 0,
):
    category = "talks"
    if start_time.weekday() == 6:
        raise ValueError("We don't have lightning talks on tutorial days")
    elif start_time.weekday() in {3, 4}:
        raise ValueError("We don't have lightning talks on tutorial days")
    start_time = CONFERENCE_TZ.localize(start_time)
    end_time = start_time + relativedelta(minutes=duration_minutes)
    post = frontmatter.loads("")
    sched = Schedule(
        accepted=True,
        layout="session-details",
        category=category,
        date=start_time,
        end_date=end_time,
        room=location,
        schedule_layout="full",
        presenter_slugs=["kojo-idrissa"],
        sitemap=True,
        title="Lightning Talks",
        permalink=f"/talk/lightning-talks-{start_time:%A}/".casefold(),
        track=f"t{track}",
    )
    post.metadata.update(sched.dict(exclude_unset=True))
    output_path = Path(
        f"_schedule/{category}/{sched.date.year}-{sched.date.month:0>2}-"
        f"{sched.date.day:0>2}-{sched.date.hour:0>2}-{sched.date.minute:0>2}-t{track}-{slugify(sched.title)}.md"
    )
    output_path.write_text(frontmatter.dumps(post) + "\n")
    print(f"Saved to {output_path}")


@app.command()
def process(process_presenters: bool = False, slug_max_length: int = 40):
    filenames = sorted(list(Path("_schedule").glob("**/*.md")))

    for filename in filenames:
        try:
            dirty = False
            post = frontmatter.loads(filename.read_text())

            # TODO: Re-enable once we know everything works...
            # data = Schedule(**post.metadata)
            # post.metadata.update(data.dict())

            slug = slugify(
                post["title"], max_length=slug_max_length, word_boundary=True
            )
            if isinstance(post["date"], str):
                # NOTE if you get weird results in 2022+ importing from papercall,
                # switch this to date = maya.when(post["date"]).datetime(
                #    to_timezone="US/Central", naive=True
                # )
                date = parse(post["date"]).astimezone(CONFERENCE_TZ)
            else:
                date = post["date"].astimezone(CONFERENCE_TZ)

            category = post.get("category")

            if category in ["break", "lunch", "social-hour"]:
                category = "talk"

            category_plural = inflection.pluralize(category)

            permalink = post.get("permalink")
            presenters = post.get("presenters", list())
            track = post.get("track")

            if permalink:
                permalink = "/".join(["", category_plural, slug, ""])
                post["permalink"] = permalink
                dirty = True

            if process_presenters:
                if presenters and len(presenters):
                    post["presenter_slugs"] = []
                    for presenter in presenters:
                        presenter = presenter.copy()
                        presenter_name = presenter.get("name")

                        if presenter_name:
                            presenter_slug = slugify(
                                presenter_name,
                                max_length=slug_max_length,
                                word_boundary=True,
                            )
                        else:
                            presenter_slug = None

                        if presenter_slug:
                            post["presenter_slugs"].append(presenter_slug)
                            presenter_post = frontmatter.loads(presenter.get("bio", ""))
                            del presenter["bio"]
                            presenter[
                                "layout"
                            ] = "speaker-template"  # 'presenter-details'
                            presenter["permalink"] = "/".join(
                                ["", "presenters", presenter_slug, ""]
                            )
                            presenter["slug"] = presenter_slug
                            presenter_post.metadata = presenter

                            presenter_filename = Path(
                                "_presenters", f"{presenter_slug}.md"
                            )

                            if not presenter_filename.parent.exists():
                                presenter_filename.parent.mkdirs()

                            presenter_filename.write_text(
                                frontmatter.dumps(presenter_post)
                            )

                        dirty = True
                        # post["presenters"] = post["presenter_slugs"]
                        # del post["presenter_slugs"]

                if post["presenter_slugs"] and len(post["presenter_slugs"]):
                    presenter_slug = post["presenter_slugs"][0]
                    post[
                        "image"
                    ] = f"/static/img/social/presenters/{presenter_slug}.png"

            if dirty is True:
                filename.write_text(frontmatter.dumps(post) + "\n")

            if track and len(track):
                talk_filename = "-".join(
                    [
                        f"{date.year:04}",
                        f"{date.month:02}",
                        f"{date.day:02}",
                        f"{date.hour:02}",
                        f"{date.minute:02}",
                        f"{track}",
                        f"{slug}.md",
                    ]
                )

            else:
                talk_filename = "-".join(
                    [
                        f"{date.year:04}",
                        f"{date.month:02}",
                        f"{date.day:02}",
                        f"{date.hour:02}",
                        f"{date.minute:02}",
                        f"{slug}.md",
                    ]
                )

            target = Path(filename.parent, talk_filename)
            if not (filename.name == target.name):
                typer.echo(f"renaming {talk_filename} to {target}")
                filename.rename(target)

        except Exception as e:
            typer.secho(f"{filename}:: {e}", fg="red")


if __name__ == "__main__":
    app()
