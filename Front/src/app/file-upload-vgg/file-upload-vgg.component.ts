import { HttpClient, HttpErrorResponse } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-file-upload-vgg',
  templateUrl: './file-upload-vgg.component.html',
  styleUrls: ['./file-upload-vgg.component.css']
})
export class FileUploadVggComponent {
  selectedFile: File | null = null;
  predictionResult: string = '';
  errorMessage: string = '';

  constructor(private http: HttpClient) {}

  onFileSelected(event: any): void {
    if (event.target.files && event.target.files.length > 0) {
      this.selectedFile = event.target.files[0];
    }
  }

  onUpload(): void {
    if (!this.selectedFile) {
      this.errorMessage = 'Please select a file first!';
      return;
    }

    const formData = new FormData();
    formData.append('file', this.selectedFile);

    this.http.post<{ genre: string }>('http://127.0.0.1:1002/predict', formData)
      .subscribe({
        next: (response) => {
          this.predictionResult = `Predicted genre: ${response.genre}`;
          this.errorMessage = '';
        },
        error: (error: HttpErrorResponse) => {
          this.errorMessage = `Error: ${error.message}`;
          this.predictionResult = '';
        }
      });
  }
}
