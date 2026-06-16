import re

with open('templates/base.html', 'r') as f:
    content = f.read()

new_nav = '''<ul class="nav-links">
        <li><a href="/">Home</a></li>
        <li><a href="/hire-handyman">Hire a Handyman</a></li>
        <li><a href="/real-estate">Real Estate Collab</a></li>
        <li>
          <a href="/maintenance">Maintenance <span class="arrow">&#9660;</span></a>
          <div class="dropdown">
            <a href="/maintenance"><div class="d-icon">&#128295;</div><div class="d-text">All Maintenance Services<span>Overview of everything we fix</span></div></a>
            <div class="dropdown-divider"></div>
            <a href="/maintenance/repairs"><div class="d-icon">&#128295;</div><div class="d-text">General Repairs<span>Doors, walls, floors and more</span></div></a>
            <a href="/maintenance/plumbing"><div class="d-icon">&#128695;</div><div class="d-text">Plumbing<span>Licensed plumbers, fast response</span></div></a>
            <a href="/maintenance/electrical"><div class="d-icon">&#9889;</div><div class="d-text">Electrical<span>Safety switches, lighting and more</span></div></a>
            <a href="/maintenance/painting"><div class="d-icon">&#127912;</div><div class="d-text">Painting and Plastering<span>Interior, exterior and plaster repairs</span></div></a>
            <a href="/maintenance/garden"><div class="d-icon">&#127807;</div><div class="d-text">Garden and Outdoor<span>Fencing, decking and garden care</span></div></a>
            <a href="/maintenance/condition-reports"><div class="d-icon">&#128203;</div><div class="d-text">Condition Reports<span>For landlords and property managers</span></div></a>
          </div>
        </li>
        <li>
          <a href="/construction">Construction <span class="arrow">&#9660;</span></a>
          <div class="dropdown">
            <a href="/construction"><div class="d-icon">&#127959;</div><div class="d-text">All Construction Services<span>Overview of everything we build</span></div></a>
            <div class="dropdown-divider"></div>
            <a href="/construction/new-homes"><div class="d-icon">&#127968;</div><div class="d-text">New Home Builds<span>Custom homes from the ground up</span></div></a>
            <a href="/construction/renovations"><div class="d-icon">&#128296;</div><div class="d-text">Renovations<span>Kitchens, bathrooms and full home renos</span></div></a>
            <a href="/construction/extensions"><div class="d-icon">&#128208;</div><div class="d-text">Extensions and Additions<span>More space, perfectly designed</span></div></a>
            <a href="/construction/commercial"><div class="d-icon">&#127970;</div><div class="d-text">Commercial Construction<span>Offices, retail and commercial builds</span></div></a>
            <a href="/construction/knockdown-rebuild"><div class="d-icon">&#129521;</div><div class="d-text">Knockdown and Rebuild<span>Love your street, love your home</span></div></a>
            <a href="/construction/dual-occupancy"><div class="d-icon">&#127969;</div><div class="d-text">Dual Occupancy<span>Maximise your blocks value</span></div></a>
          </div>
        </li>
        <li><a href="/about">About Us</a></li>
        <li><a href="/contact" class="nav-cta">Get a Quote</a></li>
      </ul>'''

content = re.sub(r'<ul class="nav-links">.*?</ul>', new_nav, content, flags=re.DOTALL)

with open('templates/base.html', 'w') as f:
    f.write(content)

print("Navbar updated successfully!")
