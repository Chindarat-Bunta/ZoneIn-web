from django.http import HttpResponse
from django.conf import settings
import django

def home(request):
    db_engine = settings.DATABASES["default"]["ENGINE"].split(".")[-1]
    is_vercel = settings.IS_VERCEL
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ZoneIn - Django on Vercel</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }}
        body {{
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: #f8fafc;
            padding: 20px;
        }}
        .card {{
            background: rgba(30, 41, 59, 0.7);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 20px;
            padding: 40px;
            max-width: 540px;
            width: 100%;
            box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.5);
            text-align: center;
        }}
        .badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: rgba(16, 185, 129, 0.15);
            color: #34d399;
            border: 1px solid rgba(16, 185, 129, 0.3);
            border-radius: 9999px;
            padding: 6px 16px;
            font-size: 0.875rem;
            font-weight: 600;
            margin-bottom: 24px;
        }}
        .badge-dot {{
            width: 8px;
            height: 8px;
            background: #10b981;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }}
        @keyframes pulse {{
            0%, 100% {{ opacity: 1; }}
            50% {{ opacity: 0.4; }}
        }}
        h1 {{
            font-size: 2.25rem;
            font-weight: 800;
            letter-spacing: -0.025em;
            margin-bottom: 12px;
            background: linear-gradient(to right, #ffffff, #cbd5e1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        p.subtitle {{
            color: #94a3b8;
            font-size: 1rem;
            line-height: 1.6;
            margin-bottom: 32px;
        }}
        .info-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 12px;
            margin-bottom: 32px;
            text-align: left;
        }}
        .info-box {{
            background: rgba(15, 23, 42, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.05);
            padding: 14px;
            border-radius: 12px;
        }}
        .info-label {{
            font-size: 0.75rem;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 4px;
        }}
        .info-value {{
            font-size: 0.95rem;
            font-weight: 600;
            color: #e2e8f0;
        }}
        .actions {{
            display: flex;
            gap: 12px;
            justify-content: center;
        }}
        .btn {{
            display: inline-block;
            padding: 12px 24px;
            border-radius: 10px;
            text-decoration: none;
            font-weight: 600;
            font-size: 0.95rem;
            transition: all 0.2s ease;
        }}
        .btn-primary {{
            background: #3b82f6;
            color: #ffffff;
            box-shadow: 0 4px 14px rgba(59, 130, 246, 0.4);
        }}
        .btn-primary:hover {{
            background: #2563eb;
            transform: translateY(-1px);
        }}
        .btn-secondary {{
            background: rgba(255, 255, 255, 0.08);
            color: #cbd5e1;
            border: 1px solid rgba(255, 255, 255, 0.1);
        }}
        .btn-secondary:hover {{
            background: rgba(255, 255, 255, 0.15);
            color: #ffffff;
        }}
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">
            <span class="badge-dot"></span>
            {'Deployed on Vercel' if is_vercel else 'Running Locally'}
        </div>
        <h1>ZoneIn Web</h1>
        <p class="subtitle">Your Django application is configured and ready for production on Vercel Serverless Functions.</p>
        
        <div class="info-grid">
            <div class="info-box">
                <div class="info-label">Framework</div>
                <div class="info-value">Django {django.get_version()}</div>
            </div>
            <div class="info-box">
                <div class="info-label">Database</div>
                <div class="info-value">{db_engine}</div>
            </div>
            <div class="info-box">
                <div class="info-label">Static Files</div>
                <div class="info-value">WhiteNoise Active</div>
            </div>
            <div class="info-box">
                <div class="info-label">Debug Mode</div>
                <div class="info-value">{'Enabled' if settings.DEBUG else 'Disabled'}</div>
            </div>
        </div>

        <div class="actions">
            <a href="/admin/" class="btn btn-primary">Django Admin</a>
            <a href="https://vercel.com/docs" target="_blank" class="btn btn-secondary">Vercel Docs</a>
        </div>
    </div>
</body>
</html>"""
    return HttpResponse(html_content)
