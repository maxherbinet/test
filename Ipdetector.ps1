while ($true) {
    try {
        # Fetch the IP using a basic GET request
        $ip = Invoke-RestMethod -uri "https://ipconfig.io/ip" -ErrorAction Stop
        
        # Get the current time
        $timestamp = Get-Date -Format "HH:mm:ss"
        
        Write-Host "[$timestamp] Current External IP: $ip" -ForegroundColor Cyan
    }
    catch {
        Write-Host "[$(Get-Date -Format 'HH:mm:ss')] Request failed. Potential failover in progress..." -ForegroundColor Yellow
    }

    Start-Sleep -Seconds 3
}