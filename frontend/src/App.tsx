import './App.css'

function App() {
  return (
    <div className="app-shell">
      <header className="topbar">
        <a className="brand" href="/" aria-label="QuickConnect home">
          <span className="brand-mark" aria-hidden="true">Q</span>
          <span>QuickConnect</span>
        </a>
        <span className="topbar-label">Volunteer workspace</span>
      </header>

      <main className="main-content">
        <section className="welcome" aria-labelledby="page-title">
          <p className="eyebrow">VOLUNTEER SPACE</p>
          <h1 id="page-title">Help nearby, when you can.</h1>
          <p className="welcome-copy">
            Your volunteer workspace will bring availability, nearby requests,
            and active assignments together in one place.
          </p>
        </section>

        <section className="location-notice" aria-labelledby="location-title">
          <div className="notice-indicator" aria-hidden="true" />
          <div>
            <h2 id="location-title">Location sharing is off</h2>
            <p>
              When you choose to be available, QuickConnect uses your browser
              location while this page is open. You can stop sharing by
              switching off availability.
            </p>
          </div>
        </section>

        <section className="workspace-card" aria-labelledby="workspace-title">
          <div className="card-heading">
            <div>
              <p className="eyebrow">YOUR WORKSPACE</p>
              <h2 id="workspace-title">A clear view of what needs you</h2>
            </div>
            <span className="setup-label">Setup in progress</span>
          </div>
          <div className="workspace-grid">
            <article className="workspace-item">
              <span className="item-number">01</span>
              <h3>Your availability</h3>
              <p>Choose when you can receive requests.</p>
            </article>
            <article className="workspace-item">
              <span className="item-number">02</span>
              <h3>Nearby requests</h3>
              <p>Review offers that match your skills and location.</p>
            </article>
            <article className="workspace-item">
              <span className="item-number">03</span>
              <h3>Active assignments</h3>
              <p>Keep track of accepted requests and next steps.</p>
            </article>
          </div>
        </section>
      </main>

      <footer className="footer">
        <span>QuickConnect</span>
        <span>For urgent, life-threatening situations, contact local emergency services.</span>
      </footer>
    </div>
  )
}

export default App
