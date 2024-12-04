import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { FileUploadComponent } from './file-upload/file-upload.component';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { FileUploadVggComponent } from './file-upload-vgg/file-upload-vgg.component';

@NgModule({
  declarations: [
    AppComponent,
    FileUploadComponent,
    FileUploadVggComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
    
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
