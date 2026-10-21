from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

HERE = os.path.dirname(os.path.abspath(__file__))
F = os.path.join(HERE, "fonts")
pdfmetrics.registerFont(TTFont("PF", os.path.join(F, "PlayfairDisplay-Regular.ttf")))
pdfmetrics.registerFont(TTFont("PFsb", os.path.join(F, "PlayfairDisplay-SemiBold.ttf")))
pdfmetrics.registerFont(TTFont("DMl", os.path.join(F, "DMSans-Light.ttf")))
pdfmetrics.registerFont(TTFont("DMr", os.path.join(F, "DMSans-Regular.ttf")))
pdfmetrics.registerFont(TTFont("DMm", os.path.join(F, "DMSans-Medium.ttf")))

FOREST   = HexColor("#162E28")
SAGE     = HexColor("#7AAE86")
SAGEPALE = HexColor("#EAF5EC")
BORDER   = HexColor("#C8DDD0")
MUTED    = HexColor("#6A8278")
BODY     = HexColor("#2E4438")
WHITE    = HexColor("#FFFFFF")

PW, PH = landscape(letter)          # 792 x 612
M = 36
CW = PW - 2 * M                     # 720

def tracked(c, x, y, text, font, size, color, sp):
    to = c.beginText(x, y); to.setFont(font, size)
    to.setFillColor(color); to.setCharSpace(sp)
    to.textOut(text); to.setCharSpace(0); c.drawText(to)

def eyebrow(c, x, y, text, color=SAGE, size=8.5, rule=True):
    if rule:
        c.setStrokeColor(color); c.setLineWidth(1.5)
        c.line(x, y + 2.6, x + 20, y + 2.6)
        x += 28
    tracked(c, x, y, text.upper(), "DMm", size, color, size * 0.20)

def wrap(c, text, font, size, maxw):
    c.setFont(font, size)
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(t, font, size) <= maxw:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur: lines.append(cur)
    return lines

def para(c, x, y, text, font, size, leading, color, maxw):
    c.setFillColor(color)
    for ln in wrap(c, text, font, size, maxw):
        c.setFont(font, size); c.drawString(x, y, ln); y -= leading
    return y

COLS = [("Food", 128), ("Date tested", 88), ("Same day", 142),
        ("Next day", 142), ("Day 3", 142), ("Verdict", 78)]
ROWS = 10
RH = 35.5
HDR_H = 25

def header(c, title, eyb):
    try:
        c.drawImage(os.path.join(HERE, "logo.jpg"), M, PH - M - 48,
                    width=96, height=60, mask=None, preserveAspectRatio=True, anchor="sw")
    except Exception:
        pass
    y = PH - M - 20
    eyebrow(c, M + 112, y + 16, eyb)
    c.setFont("PF", 25); c.setFillColor(FOREST)
    c.drawString(M + 112, y - 10, title)
    c.setStrokeColor(BORDER); c.setLineWidth(0.8)
    c.line(M, PH - M - 62, PW - M, PH - M - 62)
    return PH - M - 86

def tracker_page(c, form):
    y = header(c, "Your Reintroduction Tracker", "Reintroduction Fortnight")
    y = para(c, M,  y,
             "One food at a time. A proper portion, twice in one day. Then three days of eating as you were "
             "while you watch what happens.", "DMr", 10.5, 15, BODY, CW)
    y = para(c, M, y - 2,
             "Write it down even when nothing happens. Nothing is the result you are hoping for, and it is the "
             "one people forget to record.", "DMl", 9.5, 13.5, MUTED, CW)
    y -= 16

    # header row
    ty = y
    c.setFillColor(SAGEPALE)
    c.rect(M, ty - HDR_H, CW, HDR_H, stroke=0, fill=1)
    x = M
    c.setFont("DMm", 8.5)
    for label, w in COLS:
        tracked(c, x + 9, ty - HDR_H + 9, label.upper(), "DMm", 8.5, FOREST, 0.9)
        x += w
    # grid
    table_h = HDR_H + ROWS * RH
    c.setStrokeColor(BORDER); c.setLineWidth(0.7)
    c.rect(M, ty - table_h, CW, table_h, stroke=1, fill=0)
    for i in range(ROWS + 1):
        yy = ty - HDR_H - i * RH
        c.line(M, yy, M + CW, yy)
    x = M
    for label, w in COLS[:-1]:
        x += w
        c.line(x, ty - table_h, x, ty)

    # invisible fillable fields
    for r in range(ROWS):
        x = M
        cy = ty - HDR_H - (r + 1) * RH
        for ci, (label, w) in enumerate(COLS):
            form.textfield(name=f"r{r+1}c{ci+1}", x=x + 3, y=cy + 3,
                           width=w - 6, height=RH - 6,
                           borderWidth=0, borderColor=None, fillColor=None,
                           textColor=BODY, fontName="Helvetica", fontSize=9,
                           relative=False, forceBorder=False)
            x += w

    by = ty - table_h - 18
    c.setFont("DMm", 9); c.setFillColor(FOREST)
    c.drawString(M, by, "Verdict, three options and no others:")
    off = pdfmetrics.stringWidth("Verdict, three options and no others:", "DMm", 9) + 6
    for word in ("fine", "not yet", "no"):
        c.setFont("DMm", 9); c.setFillColor(SAGE)
        c.drawString(M + off, by, word)
        off += pdfmetrics.stringWidth(word, "DMm", 9)
        if word != "no":
            c.setFillColor(MUTED); c.setFont("DMl", 9)
            c.drawString(M + off, by, " / "); off += pdfmetrics.stringWidth(" / ", "DMl", 9)

    c.setFont("DMl", 8.5); c.setFillColor(MUTED)
    c.drawRightString(PW - M, by, "Go Happy Belly   |   gohappybelly.com")
    c.setFont("DMl", 8.5); c.setFillColor(MUTED)
    c.drawString(M, by - 15, "Print as many copies as you need. Turn over for how to run a test.")

def guide_page(c):
    y = header(c, "How To Run A Test", "Reintroduction Fortnight")
    colw = (CW - 40) / 2
    left_x, right_x = M, M + colw + 40

    def block(x, yy, head, paras):
        c.setFont("DMm", 10); c.setFillColor(FOREST)
        c.drawString(x, yy, head); yy -= 16
        for p in paras:
            yy = para(c, x, yy, p, "DMl", 9.5, 14, BODY, colw) - 8
        return yy

    ly = y
    ly = block(left_x, ly, "The method", [
        "Pick one food. Eat a proper portion of it, twice in one day. Not a taste, and not all day long.",
        "Then eat as you were for three days while you watch what happens. Do not test anything else in that window.",
        "Record something in every row, including the days nothing happens at all."])
    ly = block(left_x, ly - 4, "What counts as a reaction", [
        "Bloating, wind, a change in your bowels, reflux, skin, headache, joint aches, mood, sleep, or energy that "
        "drops off a cliff. Your pattern will have its own tell, and you will know it by now.",
        "Reactions are often slow. Something that looks fine on the day can show up on day two."])
    ly = block(left_x, ly - 4, "Pace", [
        "Three days between foods as a rule. Your pattern page may tell you to go slower, and the Reactive pattern "
        "is asked for four, because it reacts late more often than the others.",
        "Do not run a test during a brutal week. You will read the week as the food."])

    ry = y
    ry = block(right_x, ry, "The three verdicts", [
        "Fine. Nothing happened. The food goes back into your range.",
        "Not yet. Something happened, but mildly, or you are not certain. Park the food and test it again in a "
        "couple of months. This is the most common result and it is not a failure.",
        "No. A clear reaction you would not want to repeat. Leave it out and bring it to your call."])
    ry = block(right_x, ry - 4, "If you are not sure", [
        "Treat it as not yet and move on. An uncertain result you record honestly is worth more than a confident "
        "one you talked yourself into."])
    ry = block(right_x, ry - 4, "When to stop", [
        "If everything you test causes a reaction, stop testing and book your call. That means the work needs more "
        "time, not that your list is now permanent."])

    # closing band, placed under whichever column ran longer
    band_top = min(ly, ry) - 18
    inner = CW - 48
    lines = wrap(c, "A completed tracker is the most useful thing you can put in front of Alina, because it is real "
                    "evidence about your body rather than a description of how you think things have been going.",
                 "DMl", 10, inner)
    band_h = 26 + len(lines) * 15
    c.setFillColor(SAGEPALE)
    c.rect(M, band_top - band_h, CW, band_h, stroke=0, fill=1)
    c.setFillColor(SAGE); c.rect(M, band_top - band_h, 3, band_h, stroke=0, fill=1)
    ty = band_top - 20
    for ln in lines:
        c.setFont("DMl", 10); c.setFillColor(FOREST)
        c.drawString(M + 24, ty, ln); ty -= 15

    c.setFont("DMl", 8.5); c.setFillColor(MUTED)
    c.drawString(M, M + 10, "Go Happy Belly")
    c.drawRightString(PW - M, M + 10, "gohappybelly.com")

out = "/home/user/gohappybelly/Course/downloads/gohappybelly-reintroduction-tracker.pdf"
c = canvas.Canvas(out, pagesize=landscape(letter))
c.setTitle("Go Happy Belly - Reintroduction Tracker")
c.setAuthor("Go Happy Belly")
c.setSubject("Reintroduction Fortnight tracking sheet")
form = c.acroForm
tracker_page(c, form)
c.showPage()
guide_page(c)
c.save()
print("written", out, os.path.getsize(out), "bytes")
