# Ensure UTF-8 encoding
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
chcp 65001  # Set Windows console to UTF-8 code page

# Command-line argument parsing
$translated_text = $args[0]
$voice_gender = $args[1]
$voice_language = $args[2]
$output_path = $args[3]

# Log received parameters
Write-Host "Received Parameters:"
Write-Host "translated_text: $translated_text"
Write-Host "voice_gender: $voice_gender"
Write-Host "voice_language: $voice_language"
Write-Host "output_path: $output_path"

# Run inference
# try {
#     Set-Location "E:\Projects\Multilingual_TTS\Fastspeech2_HS"
    
#     $command = "python inference.py --sample_text ""$translated_text"" --language ""$voice_language"" --gender ""$voice_gender"" --alpha 1 --output_file ""$output_path"""
#     Write-Host "Executing command: $command"
    
#     Invoke-Expression $command
# }
# catch {
#     Write-Host "Error occurred while running inference.py: $_"
#     throw
# }

try {
    cd "E:\Projects\Multilingual_TTS\Fastspeech2_HS"
    python inference.py --sample_text $translated_text --language $voice_language --gender $voice_gender --alpha 1 --output_file $output_path
}
catch {
    Write-Host "Error occurred while running inference.py: $_"
}