# -*- coding: utf-8 -*-

from django.db import models

class ProjectID(models.Model):
    project = models.CharField(max_length=255)

    def __str__(self):
        return ("{} ({}/{} reviewed)"
                .format(self.project,
                        TextBlob.objects.filter(project=self.id)
                                        .filter(reviewed=True)
                                        .count(),
                        TextBlob.objects.filter(project=self.id).count(),))

class TextBlob(models.Model):
    # Project ID linking to project above
    project = models.ForeignKey(ProjectID, on_delete=models.PROTECT)

    # EDGAR specific fields for linking to EDGAR website
    cik = models.IntegerField(blank=True, null=True)
    accession = models.CharField(blank=True, null=True, max_length=20)
    edgarfname = models.CharField(max_length=255, blank=True, null=True)

    # Scraped data to be displayed
    text = models.TextField(null=True, blank=True)

    # General data added in review
    notes = models.TextField(blank=True, null=True)
    reviewed = models.BooleanField('Has been reviewed', default=False)
    flag_for_review = models.BooleanField('Flag for further review', default=False)

    # Specific data to be gathered by RA
    scrape_worked = models.BooleanField('Text was properly scraped', default=False)
    extract_number = models.IntegerField('Extracted number from text', blank=True, null=True)
    extract_text = models.CharField('Extracted excerpt from text',
                                     max_length=32, blank=True, null=True)
    # More can be added as the project progresses

    # Dates to track DB adding/updating
    add_date = models.DateField('date added', auto_now_add=True)
    update_date = models.DateTimeField('date reviewed', auto_now=True)

    def __str__(self):
        """
        Some pretty printing, displays Project name and ID when printed.
        """
        return "{}: {}".format(self.project, self.id)

    def save(self, *args, **kwargs):
        """
        Some convenience functions when 'saving' the records.
        If the RA enters any data in the fields, automatically set the
        `reviewed` field to True.
        This saves them a click.

        You can also add more logic here, like if they enter extract_number,
        maybe automatically set scrape_worked = True, etc.
        """
        if (self.scrape_worked
            or self.flag_for_review
            or self.notes is not None
            or self.extract_number is not None
            or self.extract_text is not None):
            self.reviewed = True

        # Call the "real" save() method.
        super().save(*args, **kwargs)
