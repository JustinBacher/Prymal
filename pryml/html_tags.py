from .html_core import HTMLElement

"""
Main root

This page lists all the HTML elements, which are created using tags.

They are grouped by function to help you find what you have in mind easily. An
alphabetical list of all elements is provided in the sidebar on every
element's page as well as this one.

https://developer.mozilla.org/en-US/docs/Web/HTML/Element
"""


class html(HTMLElement):
    """
    Represents the root (top-level element) of an HTML document, so it is also
    referred to as the root element. All other elements must be descendants
    of this element.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/html
    """

    pass


"""
Document metadata

Metadata contains information about the page. This includes information about
styles, scripts and data to help software (search engines, browsers, etc.) use
and render the page. Metadata for styles and scripts may be defined in the 
page or linked to another file that has the information.


https://developer.mozilla.org/en-US/docs/Web/HTML/Element#main_root
"""


class base(HTMLElement):
    """
    Specifies the base URL to use for all relative URLs in a document. There
    can be only one such element in a document.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/base
    """

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.self_closing = True


class head(HTMLElement):
    """
    Contains machine-readable information (metadata) about the document, like
    its title, scripts, and style sheets.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/head
    """

    pass


class link(HTMLElement):
    """
    Specifies relationships between the current document and an external
    resource. This element is most commonly used to link to CSS but is also
    used to establish site icons (both "favicon" style icons and icons for the
    home screen and apps on mobile devices) among other things.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/link
    """

    self_closing = True


class meta(HTMLElement):
    """
    Represents metadata that cannot be represented by other HTML meta-related
    elements, like <base>, <link>, <script>, <style> and <title>.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meta
    """

    self_closing = True


class style(HTMLElement):
    """
    Contains style information for a document or part of a document. It
    contains CSS, which is applied to the contents of the document containing
    this element.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/style
    """

    pass


class title(HTMLElement):
    """
    Defines the document's title that is shown in a browser's title bar or a
    page's tab. It only contains text; tags within the element are ignored.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/title
    """

    pass


"""
Sectioning root

https://developer.mozilla.org/en-US/docs/Web/HTML/Element#sectioning_root
"""


class body(HTMLElement):
    """
    represents the content of an HTML document. There can be only one such
    element in a document.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/body
    """

    pass


"""
Content sectioning

Content sectioning elements allow you to organize the document content into
logical pieces. Use the sectioning elements to create a broad outline for your
page content, including header and footer navigation, and heading elements to
identify sections of content.

https://developer.mozilla.org/en-US/docs/Web/HTML/Element#content_sectioning
"""


class address(HTMLElement):
    """
    Indicates that the enclosed HTML provides contact information for a person
    or people, or for an organization.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/address
    """

    pass


class article(HTMLElement):
    """
    Represents a self-contained composition in a document, page, application,
    or site, which is intended to be independently distributable or reusable
    (e.g., in syndication). Examples include a forum post, a magazine or
    newspaper article, a blog entry, a product card, a user-submitted comment,
    an interactive widget or gadget, or any other independent item of content.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/article
    """

    pass


class aside(HTMLElement):
    """
    Represents a portion of a document whose content is only indirectly
    related to the document's main content. Asides are frequently presented as
    sidebars or call-out boxes.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/aside
    """

    pass


class footer(HTMLElement):
    """
    Represents a footer for its nearest ancestor sectioning content or
    sectioning root element. A <footer> typically contains information about
    the author of the section, copyright data, or links to related documents.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/footer
    """

    pass


class header(HTMLElement):
    """
    Represents introductory content, typically a group of introductory or
    navigational aids. It may contain some heading elements but also a logo, a
    search form, an author name, and other elements.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/header
    """

    pass


class h1(HTMLElement):
    """
    Highest level section heading.

    By default, all heading elements create a block-level box in the layout,
    starting on a new line and taking up the full width available in their
    containing block.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h6
    """

    pass


class h2(HTMLElement):
    """
    Second highest level section heading.

    By default, all heading elements create a block-level box in the layout,
    starting on a new line and taking up the full width available in their
    containing block.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h6
    """

    pass


class h3(HTMLElement):
    """
    Third highest level section heading.

    By default, all heading elements create a block-level box in the layout,
    starting on a new line and taking up the full width available in their
    containing block.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h6
    """

    pass


class h4(HTMLElement):
    """
    Fourth highest level section heading.

    By default, all heading elements create a block-level box in the layout,
    starting on a new line and taking up the full width available in their
    containing block.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h6
    """

    pass


class h5(HTMLElement):
    """
    Fifth highest level section heading.

    By default, all heading elements create a block-level box in the layout,
    starting on a new line and taking up the full width available in their
    containing block.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h6
    """

    pass


class h6(HTMLElement):
    """
    Lowest level section heading.

    By default, all heading elements create a block-level box in the layout,
    starting on a new line and taking up the full width available in their
    containing block.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/h6
    """

    pass


class hgroup(HTMLElement):
    """
    Represents a heading grouped with any secondary content, such as
    subheadings, an alternative title, or a tagline.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hgroup
    """

    pass


class main(HTMLElement):
    """
    Represents the dominant content of the body of a document. The main
    content area consists of content that is directly related to or expands
    upon the central topic of a document, or the central functionality of an
    application.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/main
    """

    pass


class nav(HTMLElement):
    """
    Represents a section of a page whose purpose is to provide navigation
    links, either within the current document or to other documents. Common
    examples of navigation sections are menus, tables of contents, and
    indexes.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/nav
    """

    pass


class section(HTMLElement):
    """
    Represents a generic standalone section of a document, which doesn't have
    a more specific semantic element to represent it. Sections should always
    have a heading, with very few exceptions.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section
    """

    pass


class search(HTMLElement):
    """
    Represents a part that contains a set of form controls or other content
    related to performing a search or filtering operation.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/search
    """

    pass


"""
Text content

Use HTML text content elements to organize blocks or sections of content
placed between the opening <body> and closing </body> tags. Important for
accessibility and SEO, these elements identify the purpose or structure of
that content.

https://developer.mozilla.org/en-US/docs/Web/HTML/Element#text_content
"""


class blockquote(HTMLElement):
    """
    Indicates that the enclosed text is an extended quotation. Usually, this
    is rendered visually by indentation. A URL for the source of the quotation
    may be given using the cite attribute, while a text representation of the
    source can be given using the <cite> element.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/blockquote
    """

    pass


class dd(HTMLElement):
    """
    Provides the description, definition, or value for the preceding term
    (<dt>) in a description list (<dl>).

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dd
    """

    pass


class div(HTMLElement):
    """
    The generic container for flow content. It has no effect on the content or
    layout until styled in some way using CSS (e.g., styling is directly
    applied to it, or some kind of layout model like flexbox is applied to its
    parent element).

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/div
    """

    pass


class dl(HTMLElement):
    """
    Represents a description list. The element encloses a list of groups of
    terms (specified using the <dt> element) and descriptions (provided by
    <dd> elements). Common uses for this element are to implement a glossary
    or to display metadata (a list of key-value pairs).

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dl
    """

    pass


class dt(HTMLElement):
    """
    Specifies a term in a description or definition list, and as such must be
    used inside a <dl> element. It is usually followed by a <dd> element;
    however, multiple <dt> elements in a row indicate several terms that are
    all defined by the immediate next <dd> element.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dt
    """

    pass


class figcaption(HTMLElement):
    """
    Represents a caption or legend describing the rest of the contents of its
    parent <figure> element.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figcaption
    """

    pass


class figure(HTMLElement):
    """
    Represents self-contained content, potentially with an optional caption,
    which is specified using the <figcaption> element. The figure, its
    caption, and its contents are referenced as a single unit.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/figure
    """

    pass


class hr(HTMLElement):
    """
    Represents a thematic break between paragraph-level elements: for example,
    a change of scene in a story, or a shift of topic within a section.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/hr
    """

    pass


class li(HTMLElement):
    """
    Represents an item in a list. It must be contained in a parent element: an
    ordered list (<ol>), an unordered list (<ul>), or a menu (<menu>). In
    menus and unordered lists, list items are usually displayed using bullet
    points. In ordered lists, they are usually displayed with an ascending
    counter on the left, such as a number or letter.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/li
    """

    pass


class menu(HTMLElement):
    """
    A semantic alternative to <ul>, but treated by browsers (and exposed
    through the accessibility tree) as no different than <ul>. It represents
    an unordered list of items (which are represented by <li> elements).

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/menu
    """

    pass


class ol(HTMLElement):
    """
    Represents an ordered list of items — typically rendered as a numbered
    list.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ol
    """

    pass


class p(HTMLElement):
    """
    Represents a paragraph. Paragraphs are usually represented in visual media
    as blocks of text separated from adjacent blocks by blank lines and/or
    first-line indentation, but HTML paragraphs can be any structural grouping
    of related content, such as images or form fields.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/p
    """

    pass


class pre(HTMLElement):
    """
    Represents preformatted text which is to be presented exactly as written
    in the HTML file. The text is typically rendered using a non-proportional,
    or monospaced, font. Whitespace inside this element is displayed as
    written.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/pre
    """

    pass


class ul(HTMLElement):
    """
    Represents an unordered list of items, typically rendered as a bulleted
    list.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ul
    """

    pass


"""
Inline text semantics

Use the HTML inline text semantic to define the meaning, structure, or style
of a word, line, or any arbitrary piece of text.

https://developer.mozilla.org/en-US/docs/Web/HTML/Element#inline_text_semantics
"""


class a(HTMLElement):
    """
    Together with its href attribute, creates a hyperlink to web pages, files,
    email addresses, locations within the current page, or anything else a
    URL can address.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/a
    """

    pass


class abbr(HTMLElement):
    """
    Represents an abbreviation or acronym.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/abbr
    """

    pass


class b(HTMLElement):
    """
    Used to draw the reader's attention to the element's contents, which are
    not otherwise granted special importance. This was formerly known as the Boldface element, and most browsers still draw the text in boldface. However, you should not use <b> for styling text or granting importance. If you wish to create boldface text, you should use the CSS font-weight property. If you wish to indicate an element is of special importance, you should use the strong element.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/b
    """

    pass


class bdi(HTMLElement):
    """
    Tells the browser's bidirectional algorithm to treat the text it contains
    in isolation from its surrounding text. It's particularly useful when a
    website dynamically inserts some text and doesn't know the directionality
    of the text being inserted.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdi
    """

    pass


class bdo(HTMLElement):
    """
    Overrides the current directionality of text, so that the text within is
    rendered in a different direction.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/bdo
    """

    pass


class br(HTMLElement):
    """
    Produces a line break in text (carriage-return). It is useful for writing
    a poem or an address, where the division of lines is significant.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/br
    """

    pass


class cite(HTMLElement):
    """
    Used to mark up the title of a cited creative work. The reference may be
    in an abbreviated form according to context-appropriate conventions
    related to citation metadata.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/cite
    """

    pass


class code(HTMLElement):
    """
    Displays its contents styled in a fashion intended to indicate that the
    text is a short fragment of computer code. By default, the content text is
    displayed using the user agent's default monospace font.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/code
    """

    pass


class data(HTMLElement):
    """
    Links a given piece of content with a machine-readable translation. If the
    content is time- or date-related, the<time> element must be used.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/data
    """

    pass


class dfn(HTMLElement):
    """
    Used to indicate the term being defined within the context of a definition
    phrase or sentence. The ancestor <p> element, the <dt>/<dd> pairing, or
    the nearest section ancestor of the <dfn> element, is considered to be the
    definition of the term.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dfn
    """

    pass


class em(HTMLElement):
    """
    Marks text that has stress emphasis. The <em> element can be nested, with
    each nesting level indicating a greater degree of emphasis.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/em
    """

    pass


class i(HTMLElement):
    """
    Represents a range of text that is set off from the normal text for some
    reason, such as idiomatic text, technical terms, and taxonomical
    designations, among others. Historically, these have been presented using
    italicized type, which is the original source of the <i> naming of this
    element.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/i
    """

    pass


class kbd(HTMLElement):
    """
    Represents a span of inline text denoting textual user input from a
    keyboard, voice input, or any other text entry device. By convention, the
    user agent defaults to rendering the contents of a <kbd> element using its
    default monospace font, although this is not mandated by the HTML standard.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/kbd
    """

    pass


class mark(HTMLElement):
    """
    Represents text which is marked or highlighted for reference or notation
    purposes due to the marked passage's relevance in the enclosing context.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/mark
    """

    pass


class q(HTMLElement):
    """
    Indicates that the enclosed text is a short inline quotation. Most modern
    browsers implement this by surrounding the text in quotation marks. This
    element is intended for short quotations that don't require paragraph
    breaks; for long quotations use the <blockquote> element.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/q
    """

    pass


class rp(HTMLElement):
    """
    Used to provide fall-back parentheses for browsers that do not support the
    display of ruby annotations using the <ruby> element. One <rp> element
    should enclose each of the opening and closing parentheses that wrap the
    <rt> element that contains the annotation's text.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rp
    """

    pass


class rt(HTMLElement):
    """
    Specifies the ruby text component of a ruby annotation, which is used to
    provide pronunciation, translation, or transliteration information for
    East Asian typography. The <rt> element must always be contained within a
    <ruby> element.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/rt
    """

    pass


class ruby(HTMLElement):
    """
    Represents small annotations that are rendered above, below, or next to
    base text, usually used for showing the pronunciation of East Asian
    characters. It can also be used for annotating other kinds of text, but
    this usage is less common.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ruby
    """

    pass


class s(HTMLElement):
    """
    Renders text with a strikethrough, or a line through it. Use the <s>
    element to represent things that are no longer relevant or no longer
    accurate. However, <s> is not appropriate when indicating document edits;
    for that, use the del and ins elements, as appropriate.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/s
    """

    pass


class samp(HTMLElement):
    """
    Used to enclose inline text which represents sample (or quoted) output
    from a computer program. Its contents are typically rendered using the
    browser's default monospaced font (such as Courier or Lucida Console).

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/samp
    """

    pass


class small(HTMLElement):
    """
    Represents side-comments and small print, like copyright and legal text,
    independent of its styled presentation. By default, it renders text within
    it one font size smaller, such as from small to x-small.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/small
    """

    pass


class span(HTMLElement):
    """
    A generic inline container for phrasing content, which does not inherently
    represent anything. It can be used to group elements for styling purposes
    (using the class or id attributes), or because they share attribute
    values, such as lang. It should be used only when no other semantic
    element is appropriate. <span> is very much like a div element, but div is
    a block-level element whereas a <span> is an inline-level element.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/span
    """

    pass


class strong(HTMLElement):
    """
    Indicates that its contents have strong importance, seriousness, or
    urgency. Browsers typically render the contents in bold type.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/strong
    """

    pass


class sub(HTMLElement):
    """
    Specifies inline text which should be displayed as subscript for solely
    typographical reasons. Subscripts are typically rendered with a lowered
    baseline using smaller text.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sub
    """

    pass


class sup(HTMLElement):
    """
    Specifies inline text which is to be displayed as superscript for solely
    typographical reasons. Superscripts are usually rendered with a raised
    baseline using smaller text.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/sup
    """

    pass


class time(HTMLElement):
    """
    Represents a specific period in time. It may include the datetime
    attribute to translate dates into machine-readable format, allowing for
    better search engine results or custom features such as reminders.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/time
    """

    pass


class u(HTMLElement):
    """
    Represents a span of inline text which should be rendered in a way that
    indicates that it has a non-textual annotation. This is rendered by
    default as a simple solid underline but may be altered using CSS.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/u
    """

    pass


class var(HTMLElement):
    """
    Represents the name of a variable in a mathematical expression or a
    programming context. It's typically presented using an italicized version
    of the current typeface, although that behavior is browser-dependent.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/var
    """

    pass


class wbr(HTMLElement):
    """
    Represents a word break opportunity—a position within text where the
    browser may optionally break a line, though its line-breaking rules would
    not otherwise create a break at that location.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/wbr
    """

    pass


"""
Image and multimedia

HTML supports various multimedia resources such as images, audio, and video.

https://developer.mozilla.org/en-US/docs/Web/HTML/Element#image_and_multimedia
"""


class area(HTMLElement):
    """
    Defines an area inside an image map that has predefined clickable areas.
    An image map allows geometric areas on an image to be associated with hyperlink.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/area
    """

    pass


class audio(HTMLElement):
    """
    Used to embed sound content in documents. It may contain one or more audio
    sources, represented using the src attribute or the source element: the
    browser will choose the most suitable one. It can also be the destination
    for streamed media, using a MediaStream.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio
    """

    pass


class img(HTMLElement):
    """
    Embeds an image into the document.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/img
    """

    pass


class map(HTMLElement):
    """
    Used with <area> elements to define an image map (a clickable link area).

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/map
    """

    pass


class track(HTMLElement):
    """
    Used as a child of the media elements, audio and video. It lets you
    specify timed text tracks (or time-based data), for example to
    automatically handle subtitles. The tracks are formatted in WebVTT format
    (.vtt files)—Web Video Text Tracks.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/track
    """

    pass


class video(HTMLElement):
    """
    Embeds a media player which supports video playback into the document. You
    can also use <video> for audio content, but the audio element may provide
    a more appropriate user experience.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video
    """

    pass


"""
Embedded content

In addition to regular multimedia content, HTML can include a variety of other
content, even if it's not always easy to interact with.

https://developer.mozilla.org/en-US/docs/Web/HTML/Element#embedded_content
"""


class embed(HTMLElement):
    """
    Embeds external content at the specified point in the document. This
    content is provided by an external application or other source of
    interactive content such as a browser plug-in.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/embed
    """

    pass


class iframe(HTMLElement):
    """
    Represents a nested browsing context, embedding another HTML page into the
    current one.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe
    """

    pass


class object(HTMLElement):
    """
    Represents an external resource, which can be treated as an image, a
    nested browsing context, or a resource to be handled by a plugin.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/object
    """

    pass


class picture(HTMLElement):
    """
    Contains zero or more <source> elements and one <img> element to offer
    alternative versions of an image for different display/device scenarios.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/picture
    """

    pass


class portal(HTMLElement):
    """
    Enables the embedding of another HTML page into the current one to enable
    smoother navigation into new pages.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/portal
    """

    pass


class source(HTMLElement):
    """
    Specifies multiple media resources for the picture, the audio element, or
    the video element. It is a void element, meaning that it has no content
    and does not have a closing tag. It is commonly used to offer the same
    media content in multiple file formats in order to provide compatibility
    with a broad range of browsers given their differing support for image
    file formats and media file formats.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source
    """

    pass


"""
SVG and MathML

You can embed SVG and MathML content directly into HTML documents, using the
<svg> and <math> elements.

https://developer.mozilla.org/en-US/docs/Web/HTML/Element#svg_and_mathml
"""


class svg(HTMLElement):
    """
    Container defining a new coordinate system and viewport. It is used as the
    outermost element of SVG documents, but it can also be used to embed an
    SVG fragment inside an SVG or HTML document.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/svg
    """

    pass


class math(HTMLElement):
    """
    The top-level element in MathML. Every valid MathML instance must be
    wrapped in it. In addition, you must not nest a second <math> element in
    another, but you can have an arbitrary number of other child elements in
    it.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/math
    """

    pass


"""
Scripting

To create dynamic content and Web applications, HTML supports the use of
scripting languages, most prominently JavaScript. Certain elements support
this capability.

https://developer.mozilla.org/en-US/docs/Web/HTML/Element#scripting
"""


class canvas(HTMLElement):
    """
    Container element to use with either the canvas scripting API or the WebGL
    API to draw graphics and animations.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/canvas
    """

    pass


class noscript(HTMLElement):
    """
    Defines a section of HTML to be inserted if a script type on the page is
    unsupported or if scripting is currently turned off in the browser.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/noscript
    """

    pass


class script(HTMLElement):
    """
    Used to embed executable code or data; this is typically used to embed or
    refer to JavaScript code. The <script> element can also be used with other
    languages, such as WebGL's GLSL shader programming language and JSON.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script
    """

    pass


"""
Demarcating edits

These elements let you provide indications that specific parts of the text
have been altered.

https://developer.mozilla.org/en-US/docs/Web/HTML/Element#demarcating_edits
"""


class _del(HTMLElement):
    """
    Represents a range of text that has been deleted from a document. This can
    be used when rendering "track changes" or source code diff information,
    for example. The <ins> element can be used for the opposite purpose: to
    indicate text that has been added to the document.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/del
    """

    pass


del_ = _del


class ins(HTMLElement):
    """
    Represents a range of text that has been added to a document. You can use
    the <del> element to similarly represent a range of text that has been
    deleted from the document.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/ins
    """

    pass


"""
Table content

The elements here are used to create and handle tabular data.

https://developer.mozilla.org/en-US/docs/Web/HTML/Element#table_content
"""


class caption(HTMLElement):
    """
    Specifies the caption (or title) of a table.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/caption
    """

    pass


class col(HTMLElement):
    """
    Defines one or more columns in a column group represented by its implicit
    or explicit parent <colgroup> element. The <col> element is only valid as
    a child of a <colgroup> element that has no span attribute defined.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/col
    """

    pass


class colgroup(HTMLElement):
    """
    Defines a group of columns within a table.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/colgroup
    """

    pass


class table(HTMLElement):
    """
    Represents tabular data—that is, information presented in a
    two-dimensional table comprised of rows and columns of cells containing
    data.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/table
    """

    pass


class tbody(HTMLElement):
    """
    Encapsulates a set of table rows (<tr> elements), indicating that they
    comprise the body of a table's (main) data.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tbody
    """

    pass


class td(HTMLElement):
    """
    A child of the <tr> element, it defines a cell of a table that contains data.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/td
    """

    pass


class tfoot(HTMLElement):
    """
    Encapsulates a set of table rows (<tr> elements), indicating that they
    comprise the foot of a table with information about the table's columns.
    This is usually a summary of the columns, e.g., a sum of the given numbers
    in a column.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tfoot
    """

    pass


class th(HTMLElement):
    """
    A child of the <tr> element, it defines a cell as the header of a group of
    table cells. The nature of this group can be explicitly defined by the
    scope and headers attributes.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/th
    """

    pass


class thead(HTMLElement):
    """
    Encapsulates a set of table rows (<tr> elements), indicating that they
    comprise the head of a table with information about the table's columns.
    This is usually in the form of column headers (<th> elements).

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/thead
    """

    pass


class tr(HTMLElement):
    """
    Defines a row of cells in a table. The row's cells can then be established
    using a mix of <td> (data cell) and <th> (header cell) elements.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/tr
    """

    pass


"""
Forms

HTML provides several elements that can be used together to create forms that
the user can fill out and submit to the website or application. Further
information about this available in the HTML forms guide.

https://developer.mozilla.org/en-US/docs/Web/HTML/Element#forms
"""


class button(HTMLElement):
    """
    An interactive element activated by a user with a mouse, keyboard, finger,
    voice command, or other assistive technology. Once activated, it
    performs an action, such as submitting a form or opening a dialog.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/button
    """

    pass


class datalist(HTMLElement):
    """
    Contains a set of <option> elements that represent the permissible or
    recommended options available to choose from within other controls.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/datalist
    """

    pass


class fieldset(HTMLElement):
    """
    Used to group several controls as well as labels (<label>) within a web
    form.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/fieldset
    """

    pass


class form(HTMLElement):
    """
    Represents a document section containing interactive controls for
    submitting information.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form
    """

    pass


class input_(HTMLElement):
    """
    Used to create interactive controls for web-based forms to accept data
    from the user; a wide variety of types of input data and control widgets
    are available, depending on the device and user agent. The <input> element
    is one of the most powerful and complex in all of HTML due to the sheer
    number of combinations of input types and attributes.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input
    """

    pass


class label(HTMLElement):
    """
    Represents a caption for an item in a user interface.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label
    """

    pass


class legend(HTMLElement):
    """
    Represents a caption for the content of its parent <fieldset>.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/legend
    """

    pass


class meter(HTMLElement):
    """
    Represents either a scalar value within a known range or a fractional value.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/meter
    """

    pass


class optgroup(HTMLElement):
    """
    Creates a grouping of options within a <select> element.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/optgroup
    """

    pass


class option(HTMLElement):
    """
    Used to define an item contained in a select, an <optgroup>, or a
    <datalist> element. As such, <option> can represent menu items in popups
    and other lists of items in an HTML document.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/option
    """

    pass


class output(HTMLElement):
    """
    Container element into which a site or app can inject the results of a
    calculation or the outcome of a user action.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/output
    """

    pass


class progress(HTMLElement):
    """
    Displays an indicator showing the completion progress of a task, typically
    displayed as a progress bar.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/progress
    """

    pass


class select(HTMLElement):
    """
    Represents a control that provides a menu of options.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/select
    """

    pass


class textarea(HTMLElement):
    """
    Represents a multi-line plain-text editing control, useful when you want
    to allow users to enter a sizeable amount of free-form text, for example,
    a comment on a review or feedback form.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/textarea
    """

    pass


"""
Interactive elements

HTML offers a selection of elements that help to create interactive user
interface objects.

https://developer.mozilla.org/en-US/docs/Web/HTML/Element#interactive_elements
"""


class details(HTMLElement):
    """
    Creates a disclosure widget in which information is visible only when the
    widget is toggled into an "open" state. A summary or label must be
    provided using the <summary> element.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/details
    """

    pass


class dialog(HTMLElement):
    """
    Represents a dialog box or other interactive component, such as a
    dismissible alert, inspector, or subwindow.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/dialog
    """

    pass


class summary(HTMLElement):
    """
    Specifies a summary, caption, or legend for a details element's disclosure
    box. Clicking the <summary> element toggles the state of the parent
    <details> element open and closed.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/summary
    """

    pass


"""
Web Components

Web Components is an HTML-related technology that makes it possible to,
essentially, create and use custom elements as if it were regular HTML. In
addition, you can create custom versions of standard HTML elements.

https://developer.mozilla.org/en-US/docs/Web/HTML/Element#web_components
"""


class slot(HTMLElement):
    """
    Part of the Web Components technology suite, this element is a placeholder
    inside a web component that you can fill with your own markup, which lets
    you create separate DOM trees and present them together.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/slot
    """

    pass


class template(HTMLElement):
    """
    A mechanism for holding HTML that is not to be rendered immediately when a
    page is loaded but may be instantiated subsequently during runtime using
    JavaScript.

    https://developer.mozilla.org/en-US/docs/Web/HTML/Element/template
    """

    pass
