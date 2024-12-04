import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FileUploadVggComponent } from './file-upload-vgg.component';

describe('FileUploadVggComponent', () => {
  let component: FileUploadVggComponent;
  let fixture: ComponentFixture<FileUploadVggComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [FileUploadVggComponent]
    });
    fixture = TestBed.createComponent(FileUploadVggComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
